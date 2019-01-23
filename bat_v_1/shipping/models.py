from django.db import models
from django.utils import timezone
from django.urls import reverse
from suppliers.models import (Order, Supplier)
from settings.models import (Currency, Status, AmazonMarket)
from products.models import (Product, AmazonProduct)
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# 1. Shipment
 ## 1.1 Shipment
 ## 1.2 ShipmentProduct
 ## 1.3 ShipmentFullfillment
 ## 1.4 ShipmentFiles

# 1. Shipment
 ## 1.3 ShipmentFullfillment
class ShipmentFullfillment(models.Model):
    center_id = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=30)
    country_code = models.CharField(max_length=30)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.center_id+": "+self.name

 ## 1.1 Shipment
class Shipment(models.Model):
    PACKING_TYPE_VALUE = (
    ('Individual','Individual'),
    ('Case-packed','Case-packed')
    )
    SHIPMENT_TYPE_VALUE = (
    ('Air','Air'),
    ('Sea','Sea')
    )

    amazonmarket = models.ForeignKey(AmazonMarket,on_delete=models.PROTECT,verbose_name="Select MarketPlace")
    name = models.CharField(max_length=200)
    order = models.ForeignKey(Order,on_delete=models.PROTECT,verbose_name="Select Order")
    packing_type = models.CharField(max_length=50,choices=PACKING_TYPE_VALUE)
    type = models.CharField(max_length=20,choices=SHIPMENT_TYPE_VALUE)
    kg_cbm_price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Kg/CBM Price")
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency")
    invoice_agent = models.ForeignKey(Supplier,on_delete=models.PROTECT,verbose_name="Select Invoice Agent",related_name="invoice_agent")
    invoice_value = models.DecimalField(max_digits=8, decimal_places=2)
    invoice_currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Invoice Currency",related_name="currency_invoice")
    carrier = models.ForeignKey(Supplier,on_delete=models.PROTECT,blank=True,null=True,verbose_name="Select Carrier", related_name="carrier")
    prepaid_vat = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prepaid VAT")
    actual_vat = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Actual VAT", blank=True,null=True)
    vat_claimed = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="VAT Claimed", blank=True,null=True)
    vat_currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select VAT Currency",related_name="currency_vat")
    pickup_date = models.DateTimeField(verbose_name="Select Pickup date",blank=True,null=True)
    eta = models.DateTimeField(verbose_name="Select ETA",blank=True,null=True)
    etd = models.DateTimeField(verbose_name="Select ETD",blank=True,null=True)
    tracking_id = models.CharField(verbose_name="Tracking ID",max_length=100,blank=True,null=True)
    amazon_shipment_id = models.CharField(max_length=30,blank=True,null=True)
    amazon_labelprep = models.CharField(max_length=50,blank=True,null=True)
    shipmentfullfillment = models.ForeignKey(ShipmentFullfillment,on_delete=models.PROTECT,blank=True,null=True)
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('shipping:shipment_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

 ## 1.2 ShipmentProduct
class ShipmentProduct(models.Model):
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE,verbose_name="Select Shipment")
    product = models.ForeignKey(Product,on_delete=models.PROTECT,verbose_name="Select Product")
    amazonproduct = models.ForeignKey(AmazonProduct,on_delete=models.PROTECT,verbose_name="Select Amazon Market Product",default="")
    quantity_send = models.IntegerField()
    quantity_received = models.IntegerField(blank=True,null=True)
    missing_units = models.IntegerField(blank=True,null=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('shipping:shipmentproduct_list', kwargs={'pk':self.shipment_id})

    def __str__(self):
        return self.product.title

 ## 1.4 ShipmentFiles
def generate_shipmentfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'shipments/{0}/files/shipment-{1}-{2}-{3}{4}'.format(instance.shipment.id, slugify(instance.shipment.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)

class ShipmentFiles(models.Model):
    title = models.CharField(max_length=100)
    file_url = models.FileField(upload_to=generate_shipmentfilename)
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE,verbose_name="Select Shipment")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
