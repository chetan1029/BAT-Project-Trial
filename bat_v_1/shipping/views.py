from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from products.models import (AmazonProduct, Box)
from shipping.models import (Shipment, ShipmentProduct, ShipmentFullfillment, ShipmentFiles, ShipmentProductOrderDelivery)
from shipping.forms import (ShipmentForm, ShipmentProductForm)
from settings.models import (Status, AmazonMwsauth, AmazonMarket)
from suppliers.models import (Supplier, PaymentTerms, Contact, Bank, Contract,
                              ProductPrice, Mold, MoldFile, MoldHost, Aql,
                              Order, OrderProduct, OrderFile, OrderPayment,
                              OrderDelivery, OrderDeliveryProduct, Certification, OrderDeliveryTestReport)
from django.db.models import Q
from django.contrib import messages
import requests
import logging
import tempfile
import math
from django.core.files import File

logger = logging.getLogger(__name__)

# Create your views here.
# 1. Shipment
 ## 1.1 Shipment
  ### 1.1.1 ShipmentListView
  ### 1.1.2 ShipmentDetailView
  ### 1.1.3 CreateShipmentView
  ### 1.1.4 ShipmentUpdateView
  ### 1.1.5 ShipmentDeleteView
 ## 1.2 ShipmentProduct
  ### 1.2.1 ShipmentProductListView
  ### 1.2.2 CreateShipmentProductView
  ### 1.2.3 ShipmentProductUpdateView
  ### 1.2.4 ShipmentProductDeleteView

# 1. Shipment
 ## 1.1 Shipment
  ### 1.1.1 ShipmentListView
class ShipmentListView(LoginRequiredMixin,ListView):
    model = Shipment
    template_name = 'shipment/shipment_list.html'

    def get_queryset(self):
        return Shipment.objects.filter(Q(status__title="Pending") | Q(status__title="Ready for Amazon") | Q(status__title="Working"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"pending"}
        return context

  ### 1.1.1 ReadytoshipView
class ReadytoshipView(LoginRequiredMixin,ListView):
    model = Shipment
    template_name = 'shipment/ready_to_ship.html'

    def get_queryset(self):
        self.orderdelivery = OrderDelivery.objects.filter(status__title="Ready To Ship")
        return Shipment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"ready_to_ship"}
        context['orderdeliveries'] = self.orderdelivery
        return context

def create_shipment(request):
    if request.method == 'POST':
        shipment_type = request.POST.get('shipment_type',False)
        orderdelivery_ids = request.POST.getlist('orderdelivery_id')
        active = {"menu1":"basic","menu2":"shipping","menu3":"ready_to_ship"}
        shipment_plan = []
        if shipment_type and orderdelivery_ids:
            shipment_plan1 = {}
            shipment_products = []
            for orderdelivery_id in orderdelivery_ids:
                orderdelivery = OrderDelivery.objects.get(pk=orderdelivery_id)
                orderbatch_id = orderdelivery.batch_id
                orderdeliveryproduct_ids = request.POST.getlist('orderdeliveryproduct'+str(orderdelivery_id))
                if orderdeliveryproduct_ids:
                    for orderdeliveryproduct_id in orderdeliveryproduct_ids:
                        orderdeliveryproduct = OrderDeliveryProduct.objects.get(pk=orderdeliveryproduct_id)
                        orderproduct_id = orderdeliveryproduct.orderproduct_id
                        quantity = request.POST.get('quantity'+str(orderdeliveryproduct_id),False)
                        if int(quantity) is not None and int(quantity) != 0:
                            shipment_plan_product = {}
                            shipment_plan_product["orderproduct_id"] = orderproduct_id
                            shipment_plan_product["orderproduct_quantity"] = quantity
                            shipment_plan_product["orderdelivery_id"] = orderdelivery_id
                            shipment_plan_product["orderbatch_id"] = orderbatch_id
                            shipment_plan_product["orderdeliveryproduct_id"] = orderdeliveryproduct_id
                            shipment_products.append(shipment_plan_product)
                            logger.warning("InsideQ:"+str(quantity))
                shipment_products.sort(key=lambda e: e['orderproduct_id'], reverse=True)
                new_shipment_plan = {}
                for p in shipment_products:
                    id = p['orderproduct_id']
                    if id not in new_shipment_plan:
                        new_shipment_plan[id] = []
                    d = { 'orderproduct_quantity': p['orderproduct_quantity'],
                          'orderbatch_id': p['orderbatch_id'],
                          'orderdeliveryproduct_id': p['orderdeliveryproduct_id'],
                          'orderdelivery_id': p['orderdelivery_id'] }
                    new_shipment_plan[id].append(d)
                #logger.warning(new_shipment_plan)
                shipment_plan = []
                for k, v in new_shipment_plan.items():
                    orderproduct = OrderProduct.objects.get(pk=k)
                    product_id = orderproduct.productprice.product.pk
                    product_title = orderproduct.productprice.product.title
                    product_image = orderproduct.productprice.product.image
                    shipment_plan.append({ 'orderproduct_id': k , 'product_id':product_id, 'product_title':product_title, 'product_image':product_image, 'batches': v })

            #logger.warning(shipment_plan)
            markets = AmazonMarket.objects.all()
            return render(request, 'shipment/create-shipment.html' ,{'shipment_type': shipment_type,'shipment_plan': shipment_plan, 'active_menu':active, 'markets':markets})
        else:
            if not shipment_type:
                error = "Please select shipment type"
                messages.error(request, error)
            if not orderdelivery_ids:
                error = "Please select order partial delivery"
                messages.error(request, error)
            return redirect('shipping:ready_to_ship')

def submit_shipment_data(request):
    if request.method == 'POST':
        shipment_status = Status.objects.get(title= "Shipping", parent__isnull=True)
        planning_status = Status.objects.get(title="Planning", parent=shipment_status)
        pending_status = Status.objects.get(title="Pending", parent=shipment_status)

        packing_type = "Individual"
        shipment_type = request.POST.get('shipment_type',False)
        product_ids = request.POST.getlist('product_id')
        if shipment_type and product_ids:
            for product_id in product_ids:
                market_ids = request.POST.getlist('market'+str(product_id))
                if market_ids:
                    for market_id in market_ids:
                        amazonmarket = AmazonMarket.objects.get(pk=market_id)
                        if Shipment.objects.filter(amazonmarket_id=market_id, status__title="Planning").exists():
                            shipment = Shipment.objects.get(amazonmarket_id=market_id, status__title="Planning")
                        else:
                            shipment = Shipment(amazonmarket_id=market_id,name="Shipment",packing_type=packing_type,type=shipment_type,status=planning_status)
                            shipment.save()
                            shipment.name = amazonmarket.country_code+"-"+str(shipment.pk)
                            shipment.save()
                        amazonproduct = AmazonProduct.objects.get(product_id=product_id)
                        shipmentproduct = ShipmentProduct(shipment_id=shipment.pk,product_id=product_id,amazonproduct_id=amazonproduct.pk,quantity_send=0)
                        shipmentproduct.save()
                        orderdelivery_ids = request.POST.getlist('orderdelivery'+str(product_id)+''+str(market_id),False)
                        total_quantity = 0
                        if orderdelivery_ids:
                            for orderdelivery_id in orderdelivery_ids:
                                orderdeliveryproduct_id = request.POST.get('orderdeliveryproduct'+str(product_id)+''+str(market_id)+''+str(orderdelivery_id),False)
                                quantity = request.POST.get('quantity'+str(product_id)+''+str(market_id)+''+str(orderdelivery_id),False)
                                if quantity:
                                    shipmentproductorderdelivery = ShipmentProductOrderDelivery(shipmentproduct=shipmentproduct, orderdelivery_id=orderdelivery_id, quantity=quantity, orderdeliveryproduct_id=orderdeliveryproduct_id)
                                    shipmentproductorderdelivery.save()
                                    total_quantity += int(quantity)
                                    logger.warning("shipment_type: "+shipment_type+", "+str(product_id)+", "+str(market_id)+", "+orderdelivery_id+", "+quantity)
                        shipmentproduct.quantity_send=total_quantity
                        shipmentproduct.save()
        Shipment.objects.filter(status__title="Planning").update(status=pending_status)

    return redirect('shipping:shipment_list')

  ### 1.1.2 ShipmentDetailView
class ShipmentDetailView(LoginRequiredMixin,DetailView):
    model = Shipment
    template_name = 'shipment/shipment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"detail"}
        return context

  ### 1.1.3 CreateShipmentView
class CreateShipmentView(LoginRequiredMixin,CreateView):
    form_class = ShipmentForm
    model = Shipment
    template_name = 'shipment/shipment_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.object.amazonmarket.country_code+"-"+timezone.now().strftime("%Y%m%d")+"-"+self.object.type
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment"}
        return context

  ### 1.1.4 ShipmentUpdateView
class ShipmentUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ShipmentForm
    model = Shipment
    template_name = 'shipment/shipment_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        status = Shipment.objects.get(pk=self.object.pk).status.title
        if status == "Pending":
            if self.object.kg_cbm_price and self.object.currency and self.object.invoice_agent and self.object.invoice_value and self.object.invoice_currency and self.object.pickup_date and self.object.eta and self.object.etd and self.object.bol_number:
                shipment_status = Status.objects.get(title= "Shipping", parent__isnull=True)
                ready_for_amazon_status = Status.objects.get(title="Ready for Amazon", parent=shipment_status)
                self.object.status = ready_for_amazon_status
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment"}
        context['form'].fields['invoice_agent'].queryset = Supplier.objects.filter(category__name="Agent")
        return context

  ### 1.1.5 ShipmentDeleteView
class ShipmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Shipment
    template_name = 'shipment/shipment_confirm_delete.html'
    success_url = reverse_lazy('shipping:shipment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment"}
        return context

 ## 1.2 ShipmentProduct
  ### 1.2.1 ShipmentProductListView
class ShipmentProductListView(LoginRequiredMixin,ListView):
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_list.html'

    def get_queryset(self):
        shipment_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=shipment_id)
        return ShipmentProduct.objects.filter(shipment_id = shipment_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        context['shipment_id'] = self.kwargs['pk']
        context['shipment'] = self.shipment
        return context

  ### 1.2.2 CreateShipmentProductView
class CreateShipmentProductView(LoginRequiredMixin,CreateView):
    form_class = ShipmentProductForm
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.shipment = Shipment.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        shipment_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=shipment_id)
        context['shipment'] = self.shipment
        context['form'].fields['product'].queryset = OrderProduct.objects.filter(order_id=self.shipment.order_id)
        return context

  ### 1.2.3 ShipmentProductUpdateView
class ShipmentProductUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ShipmentProductForm
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        shipmentproduct_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=(ShipmentProduct.objects.get(pk=shipmentproduct_id).shipment_id))
        context['shipment'] = self.shipment
        context['form'].fields['product'].queryset = OrderProduct.objects.filter(order_id=self.shipment.order_id)
        return context

  ### 1.2.4 ShipmentProductDeleteView
class ShipmentProductDeleteView(LoginRequiredMixin,DeleteView):
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_confirm_delete.html'

    def get_queryset(self):
        shipmentproduct_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=(ShipmentProduct.objects.get(pk=shipmentproduct_id).shipment_id))
        return ShipmentProduct.objects.filter(pk=shipmentproduct_id)

    def get_success_url(self):
        return reverse_lazy('shipping:shipmentproduct_list', kwargs={'pk': ShipmentProduct.objects.get(id=self.kwargs['pk']).shipment_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        context['shipment'] = self.shipment
        return context

 ## 1.3 ShipmentFiles
  ### 1.3.1 ShipmentFilesListView
class ShipmentFilesListView(LoginRequiredMixin,ListView):
    model = ShipmentFiles
    template_name = 'shipmentfiles/shipmentfiles_list.html'

    def get_queryset(self):
        shipment_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=shipment_id)
        return ShipmentFiles.objects.filter(shipment_id = shipment_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"files"}
        context['shipment_id'] = self.kwargs['pk']
        context['shipment'] = self.shipment
        return context

  ### 1.3.2 ShipmentFilesDeleteView
class ShipmentFilesDeleteView(LoginRequiredMixin,DeleteView):
    model = ShipmentFiles
    template_name = 'shipmentfiles/shipmentfiles_confirm_delete.html'

    def get_queryset(self):
        shipmentfiles_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=(ShipmentFiles.objects.get(pk=shipmentfiles_id).shipment_id))
        return ShipmentFiles.objects.filter(pk=shipmentfiles_id)

    def get_success_url(self):
        return reverse_lazy('shipping:shipmentfiles_list', kwargs={'pk': ShipmentFiles.objects.get(id=self.kwargs['pk']).shipment_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"files"}
        context['shipment'] = self.shipment
        return context

########## MWS API Calls ############
def create_amazon_shipment(request, pk):
    ## Create InboundShipmentPlan
    shipment = Shipment.objects.get(pk=pk)
    shipment_product = ShipmentProduct.objects.filter(shipment_id=pk)
    shipment_product_data = []

    total_package_boxes = 0
    for shipment_p in shipment_product:
        shipment_product_data1 = {}
        shipment_product_data1["SellerSKU"] = shipment_p.amazonproduct.seller_sku
        shipment_product_data1["Quantity"] = shipment_p.quantity_send
        shipment_product_data1["UnitsPerBox"] = Box.objects.get(product=shipment_p.product,type="Active").units_per_box
        total_package_boxes += math.ceil(shipment_product_data1["Quantity"]/shipment_product_data1["UnitsPerBox"])
        shipment_product_data.append(shipment_product_data1)

    amazonmwsauth = AmazonMwsauth.objects.get(region=shipment.amazonmarket.region)
    amazon_auth = {}
    amazon_auth["MarketPlaceId"] = shipment.amazonmarket.marketplace_id
    amazon_auth["SellerId"] = amazonmwsauth.seller_id
    amazon_auth["MWSAuthToken"] = amazonmwsauth.auth_token
    amazon_auth["AccessKey"] = amazonmwsauth.access_key
    amazon_auth["SecretKey"] = amazonmwsauth.secret_key

    shipment_data = {
    "LabelPrepPreference": "SELLER_LABEL",
    "ShipmentType": shipment.type,
    "Name": shipment.invoice_agent.name,
    "AddressLine1": shipment.invoice_agent.address1,
    "AddressLine2": shipment.invoice_agent.address2,
    "City": shipment.invoice_agent.city,
    "StateOrProvinceCode": shipment.invoice_agent.region_code,
    "PostalCode": shipment.invoice_agent.zip,
    "CountryCode": shipment.invoice_agent.country_code,
    "ShipToCountryCode": shipment.amazonmarket.country_code,
    "domain": shipment.amazonmarket.amazon_id,
    "shipment_product": shipment_product_data,
    "amazon_auth": amazon_auth
    }

    #logger.warning(shipment_data)

    response = requests.post("http://174.138.71.123/amazon/shipments/api/createinboundshipmentplan.php", json=shipment_data)
    response_data = response.json()
    #logger.warning(response_data)

    if ShipmentFullfillment.objects.filter(center_id=response_data["fulfillmentcenter"]).exists():
        fullfillmentcenter = ShipmentFullfillment.objects.get(center_id=response_data["fulfillmentcenter"])
    else:
        fullfillmentcenter = ShipmentFullfillment.objects.create(center_id=response_data["fulfillmentcenter"],name=response_data["fulfillment_name"],address_line1=response_data["fulfillment_address1"],city=response_data["fulfillment_city"],state=response_data["fulfillment_state"],postal_code=response_data["fulfillment_postalcode"],country_code=response_data["fulfillment_countrycode"])

    shipment.amazon_shipment_id = response_data["shipment_id"]
    shipment.amazon_labelprep = response_data["labelprep"]
    shipment.shipmentfullfillment = fullfillmentcenter
    shipment.save()

    ## Create InboundShipment
    shipment_data["ShipmentId"] = response_data["shipment_id"]
    shipment_data["ShipmentName"] = shipment.name
    shipment_data["DestinationFulfillmentCenterId"] = response_data["fulfillmentcenter"]
    shipment_data["ShipmentStatus"] = "WORKING"
    shipment_data["IntendedBoxContentsSource"] = "FEED"

    response = requests.post("http://174.138.71.123/amazon/shipments/api/createinboundshipment.php", json=shipment_data)
    response_data = response.json()
    shipment_data["ShipmentId"] = shipment.amazon_shipment_id
    response = requests.post("http://174.138.71.123/amazon/shipments/api/submitfeed.php", json=shipment_data)
    response_data = response.json()
    #logger.warning(response_data)
    shipment_data["NumberOfPackages"] = total_package_boxes
    response = requests.post("http://174.138.71.123/amazon/shipments/api/getpackagelabels.php", json=shipment_data)
    response_data = response.json()
    logger.warning(response_data)

    ## Process Packagelabels pdf file and save to ShipmentFiles Database
    box_labels_request = requests.get(response_data['file_url'], stream=True)

    box_labels_temp = tempfile.NamedTemporaryFile()
    for block in box_labels_request.iter_content(1024 * 8):
        if not block:
            break
        box_labels_temp.write(block)

    shipment_box_labels = ShipmentFiles(title="Box Labels",shipment=shipment)
    shipment_box_labels.file_url.save('box-label.pdf', File(box_labels_temp))

    shipment_data["NumberOfPallets"] = 1 # just need 1 pallet label because they are same so you shipment company print them as per pallet numbers.
    response = requests.post("http://174.138.71.123/amazon/shipments/api/getpalletlabels.php", json=shipment_data)
    response_data = response.json()
    logger.warning(response_data)

    ## Process Packagelabels pdf file and save to ShipmentFiles Database
    pallet_labels_request = requests.get(response_data['file_url'], stream=True)

    pallet_labels_temp = tempfile.NamedTemporaryFile()
    for block in pallet_labels_request.iter_content(1024 * 8):
        if not block:
            break
        pallet_labels_temp.write(block)

    shipment_pallet_labels = ShipmentFiles(title="Pallet Labels",shipment=shipment)
    shipment_pallet_labels.file_url.save('pallet-label.pdf', File(pallet_labels_temp))

    if shipment.bol_number:
        shipment_data["BOLNumber"] = shipment.bol_number
        response = requests.post("http://174.138.71.123/amazon/shipments/api/puttransportcontent.php", json=shipment_data)
        response_data = response.json()
        logger.warning(response_data)

    shipment_status = Status.objects.get(title= "Shipping", parent__isnull=True)
    working_status = Status.objects.get(title="Working", parent=shipment_status)
    shipment.status = working_status
    shipment.save()
    return redirect('shipping:shipment_detail', pk=pk)

def submit_package_info(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    logger.warning("Your log message is here")
    shipment_product = ShipmentProduct.objects.filter(shipment_id=pk)

    return redirect('shipping:shipment_detail', pk=pk)
