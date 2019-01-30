from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from shipping.models import (Shipment, ShipmentProduct, ShipmentFullfillment, ShipmentFiles)
from shipping.forms import (ShipmentForm, ShipmentProductForm)
from settings.models import (Status, AmazonMwsauth)
from suppliers.models import (Order,OrderProduct,Aql,Supplier)
from django.db.models import Q
import requests
import logging
import tempfile
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment"}
        return context

  ### 1.1.2 ShipmentDetailView
class ShipmentDetailView(LoginRequiredMixin,DetailView):
    model = Shipment
    template_name = 'shipment/shipment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment","menu4":"detail"}
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
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment"}
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Shipping'))
        return context

  ### 1.1.4 ShipmentUpdateView
class ShipmentUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ShipmentForm
    model = Shipment
    template_name = 'shipment/shipment_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment"}
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Shipping'))
        return context

  ### 1.1.5 ShipmentDeleteView
class ShipmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Shipment
    template_name = 'shipment/shipment_confirm_delete.html'
    success_url = reverse_lazy('shipping:shipment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment"}
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
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment","menu4":"product"}
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
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment","menu4":"product"}
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
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment","menu4":"product"}
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
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment","menu4":"product"}
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
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment","menu4":"files"}
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
        context['active_menu'] = {"menu1":"inventorize","menu2":"shipping","menu3":"shipment","menu4":"files"}
        context['shipment'] = self.shipment
        return context

########## MWS API Calls ############
def create_amazon_shipment(request, pk):
    ## Create InboundShipmentPlan
    shipment = Shipment.objects.get(pk=pk)
    shipment_product = ShipmentProduct.objects.filter(shipment_id=pk)
    shipment_product_data = []

    for shipment_p in shipment_product:
        shipment_product_data1 = {}
        shipment_product_data1["SellerSKU"] = shipment_p.amazonproduct.seller_sku
        shipment_product_data1["Quantity"] = shipment_p.quantity_send
        shipment_product_data1["UnitsPerBox"] = shipment_p.amazonproduct.units_per_box
        shipment_product_data.append(shipment_product_data1)

    amazonmwsauth = AmazonMwsauth.objects.get(identifier=shipment.amazonmarket.country_code)
    amazon_auth = {}
    amazon_auth["MarketPlaceId"] = shipment.amazonmarket.marketplace_id
    amazon_auth["SellerId"] = amazonmwsauth.seller_id
    amazon_auth["MWSAuthToken"] = amazonmwsauth.auth_token
    amazon_auth["AccessKey"] = amazonmwsauth.access_key
    amazon_auth["SecretKey"] = amazonmwsauth.secret_key

    shipment_data = {
    "LabelPrepPreference": "SELLER_LABEL",
    "ShipmentType": shipment.type,
    "Name": shipment.order.aql.supplier.name,
    "AddressLine1": shipment.order.aql.supplier.address1,
    "AddressLine2": shipment.order.aql.supplier.address2,
    "City": shipment.order.aql.supplier.city,
    "StateOrProvinceCode": shipment.order.aql.supplier.region_code,
    "PostalCode": shipment.order.aql.supplier.zip,
    "CountryCode": shipment.order.aql.supplier.country_code,
    "ShipToCountryCode": shipment.amazonmarket.country_code,
    "domain": shipment.amazonmarket.amazon_id,
    "shipment_product": shipment_product_data,
    "amazon_auth": amazon_auth
    }

    logger.warning(shipment_data)

    # response = requests.post("http://174.138.71.123/amazon/shipments/api/createinboundshipmentplan.php", json=shipment_data)
    # response_data = response.json()
    #
    # if ShipmentFullfillment.objects.filter(center_id=response_data["fulfillmentcenter"]).exists():
    #     fullfillmentcenter = ShipmentFullfillment.objects.get(center_id=response_data["fulfillmentcenter"])
    # else:
    #     fullfillmentcenter = ShipmentFullfillment.objects.create(center_id=response_data["fulfillmentcenter"],name=response_data["fulfillment_name"],address_line1=response_data["fulfillment_address1"],city=response_data["fulfillment_city"],state=response_data["fulfillment_state"],postal_code=response_data["fulfillment_postalcode"],country_code=response_data["fulfillment_countrycode"])
    #
    # shipment.amazon_shipment_id = response_data["shipment_id"]
    # shipment.amazon_labelprep = response_data["labelprep"]
    # shipment.shipmentfullfillment = fullfillmentcenter
    # shipment.save()
    #
    # ## Create InboundShipment
    # shipment_data["ShipmentId"] = response_data["shipment_id"]
    # shipment_data["ShipmentName"] = shipment.name
    # shipment_data["DestinationFulfillmentCenterId"] = response_data["fulfillmentcenter"]
    # shipment_data["ShipmentStatus"] = "WORKING"
    # shipment_data["IntendedBoxContentsSource"] = "FEED"
    #
    # response = requests.post("http://174.138.71.123/amazon/shipments/api/createinboundshipment.php", json=shipment_data)
    # response_data = response.json()
    shipment_data["ShipmentId"] = shipment.amazon_shipment_id
    #response = requests.post("http://174.138.71.123/amazon/shipments/api/submitfeed.php", json=shipment_data)
    #response_data = response.json()
    #logger.warning(response_data)
    shipment_data["NumberOfPackages"] = 25
    #response = requests.post("http://174.138.71.123/amazon/shipments/api/getpackagelabels.php", json=shipment_data)
    #response_data = response.json()
    #logger.warning(response_data)

    ## Process Packagelabels pdf file and save to ShipmentFiles Database
    # box_labels_request = requests.get(response_data['file_url'], stream=True)
    #
    # box_labels_temp = tempfile.NamedTemporaryFile()
    # for block in box_labels_request.iter_content(1024 * 8):
    #     if not block:
    #         break
    #     box_labels_temp.write(block)
    #
    # shipment_box_labels = ShipmentFiles(title="Box Labels",shipment=shipment)
    # shipment_box_labels.file_url.save('box-label.pdf', File(box_labels_temp))
    #
    # response = requests.post("http://174.138.71.123/amazon/shipments/api/getpalletlabels.php", json=shipment_data)
    # response_data = response.json()
    # logger.warning(response_data)
    #
    # ## Process Packagelabels pdf file and save to ShipmentFiles Database
    # pallet_labels_request = requests.get(response_data['file_url'], stream=True)
    #
    # pallet_labels_temp = tempfile.NamedTemporaryFile()
    # for block in pallet_labels_request.iter_content(1024 * 8):
    #     if not block:
    #         break
    #     pallet_labels_temp.write(block)
    #
    # shipment_pallet_labels = ShipmentFiles(title="Pallet Labels",shipment=shipment)
    # shipment_pallet_labels.file_url.save('pallet-label.pdf', File(pallet_labels_temp))

    if shipment.bol_number:
        shipment_data["BOLNumber"] = shipment.bol_number
        response = requests.post("http://174.138.71.123/amazon/shipments/api/puttransportcontent.php", json=shipment_data)
        response_data = response.json()
        logger.warning(response_data)

    return redirect('shipping:shipment_detail', pk=pk)

def submit_package_info(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    logger.warning("Your log message is here")
    shipment_product = ShipmentProduct.objects.filter(shipment_id=pk)

    return redirect('shipping:shipment_detail', pk=pk)
