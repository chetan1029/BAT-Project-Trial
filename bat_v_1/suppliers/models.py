from django.db import models
from django.utils import timezone
from django.urls import reverse
import random
from products.models import (Product)
from settings.models import (Category, Status, Currency)
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from decimal import Decimal
import os, datetime
User = get_user_model()

# Create your models here.
# 1. PaymentTerms
# 2. Supplier
 ## 2.1 Contact
 ## 2.2 Bank
 ## 2.3 Contract
 ## 2.4 ProductPrice
 ## 2.5 Mold
  ### 2.5.1 Mold
  ### 2.5.2 MoldFile
 ## 2.6 Aql
  ### 2.6.1 Aql
 ## 2.7 Order
  ### 2.7.1 Order
  ### 2.7.2 OrderProduct
  ### 2.7.3 OrderFile
  ### 2.7.4 OrderPayment
  ### 2.7.5 OrderDelivery
 ## 2.8 Certification
  ### 2.8.1 Certification

# 1. PaymentTerms
class PaymentTerms(models.Model):
    title = models.CharField(max_length=200)
    deposit = models.DecimalField(max_digits=5, decimal_places=2)
    payment_term = models.IntegerField()
    on_delivery = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Balance on delivery")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:paymentterms_list')

    def __str__(self):
        return self.title

# 2. Supplier
def generate_logofilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/logo/logo{1}'.format(instance.id, extension)

class Supplier(models.Model):
    SUPPLIER_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=SUPPLIER_OPTIONS,default="Active")
    name = models.CharField(verbose_name="Supplier Name", max_length=200)
    alternate_name = models.CharField(verbose_name="Supplier Alternative Name", max_length=200,blank=True)
    logo = models.ImageField(upload_to=generate_logofilename,blank=True)
    address1 = models.CharField(max_length=200,blank=True)
    address2 = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200,blank=True)
    zip = models.CharField(verbose_name="Zip/Pin Code",max_length=200,blank=True)
    region = models.CharField(verbose_name="State/Province",max_length=200,blank=True)
    region_code = models.CharField(verbose_name="State/Province Code",max_length=10,blank=True,default="")
    country = models.CharField(max_length=200,blank=True)
    country_code = models.CharField(max_length=10,blank=True,default="")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Select Category")
    detail = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:supplier_detail',kwargs={'pk':self.pk})

    def get_formatted_address(self):
        address = ""
        if self.address1 is None and self.address2 is None and self.city is None and self.region is None and self.country is None and self.zip is None:
            address = ""
        else:
            if self.address1:
                address += self.address1
            if self.address2:
                address += ", "+self.address2
            if self.city:
                address += "<br />"+self.city
            if self.region:
                address += ", "+self.region
            if self.region_code:
                address += " ("+self.region_code+")"
            if self.country:
                address += "<br />"+self.country
            if self.country_code:
                address += " ("+self.country_code+")"
            if self.zip:
                address += ", "+self.zip
        return address.strip(",")

    def __str__(self):
        return self.name

 ## 2.1 Contact
class Contact(models.Model):
    CONTACT_OPTIONS = (
    ('Primary','Primary'),
    ('Secondary','Secondary'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=CONTACT_OPTIONS,default="")
    job_title = models.CharField(max_length=50, default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    skype = models.CharField(max_length=50,blank=True)
    wechat = models.CharField(max_length=50,blank=True)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name="Select Supplier")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:contact_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.first_name+" "+self.last_name

 ## 2.2 Bank
class Bank(models.Model):
    BANK_TYPE_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=BANK_TYPE_OPTIONS,default="")
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200)
    zip = models.CharField(verbose_name="Zip/Pin Code",max_length=200)
    region = models.CharField(verbose_name="Region/State",max_length=200,blank=True)
    country = models.CharField(max_length=200)
    benificary = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=50)
    currency = models.ManyToManyField(Currency,verbose_name="Select Currency")
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name="Select Supplier")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:bank_list', kwargs={'pk':self.supplier_id})

    def get_formatted_address(self):
        address = ""
        if self.address1 is None and self.address2 is None and self.city is None and self.region is None and self.country is None and self.zip is None:
            address = ""
        else:
            if self.address1:
                address += self.address1
            if self.address2:
                address += ", "+self.address2
            if self.city:
                address += ", "+self.city
            if self.region:
                address += ", "+self.region
            if self.country:
                address += ", "+self.country
            if self.zip:
                address += ", "+self.zip
        return address

    def __str__(self):
        return self.name

 ## 2.3 Contract
def generate_filename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/contracts/contract-{1}-{2}{3}'.format(instance.supplier.id, slugify(instance.supplier.name), timezone.now().strftime("%Y%m%d") ,extension)

class Contract(models.Model):
    CONTRACT_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=CONTRACT_OPTIONS,default="")
    title = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name="Select Supplier")
    file_url = models.FileField(upload_to=generate_filename)
    note = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:contract_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.title

 ## 2.4 ProductPrice
class ProductPrice(models.Model):
    PRICE_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=PRICE_OPTIONS,default="Active")
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name="Select Supplier")
    product = models.ForeignKey(Product,on_delete=models.PROTECT,verbose_name="Select Product", related_name="productprice_product")
    price = models.DecimalField(max_digits=7, decimal_places=3)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:productprice_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.product.title

 ## 2.5 Mold
  ### 2.5.1 Mold
class Mold(models.Model):
    title = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier,on_delete=models.PROTECT,verbose_name="Select Supplier")
    x_units = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=3)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency")
    no_of_layers = models.IntegerField()
    paid_by = models.CharField(max_length=20)
    production_date = models.DateField()
    category = models.ManyToManyField(Category,verbose_name="Select Categories")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:mold_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.title

  ### 2.5.2 MoldFile
def generate_moldfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Molds/{1}/mold-{2}-{3}{4}'.format(instance.mold.supplier.id, instance.mold.id, slugify(instance.mold.supplier.name), timezone.now().strftime("%Y%m%d") ,extension)


class MoldFile(models.Model):
    MOLDHOST_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=MOLDHOST_OPTIONS,default="")
    note = models.TextField(blank=True)
    file_url = models.FileField(upload_to=generate_moldfilename)
    mold = models.ForeignKey(Mold,on_delete=models.PROTECT,verbose_name="Select Mold")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:moldfile_list', kwargs={'pk':self.mold_id})

    def __str__(self):
        return self.type

class MoldHost(models.Model):
    MOLDHOST_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=MOLDHOST_OPTIONS,default="")
    supplier = models.ForeignKey(Supplier,on_delete=models.PROTECT,verbose_name="Select Mold Host")
    mold = models.ForeignKey(Mold,on_delete=models.PROTECT,verbose_name="Select Mold")
    note = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:moldhost_list', kwargs={'pk':self.mold_id})

    def __str__(self):
        return self.type

 ## 2.6 Aql
  ### 2.6.1 Aql
def generate_aqlfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'me/{0}-{1}/aql-{2}{3}'.format(slugify(instance.category.name), instance.version, timezone.now().strftime("%Y%m%d") ,extension)
def generate_sopfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'me/{0}-{1}/sop-{2}{3}'.format(slugify(instance.category.name), instance.version, timezone.now().strftime("%Y%m%d") ,extension)
def generate_mdfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'me/{0}-{1}/md-{2}{3}'.format(slugify(instance.category.name), instance.version, timezone.now().strftime("%Y%m%d") ,extension)
def generate_bomfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'me/{0}-{1}/bom-{2}{3}'.format(slugify(instance.category.name), instance.version, timezone.now().strftime("%Y%m%d") ,extension)
def generate_ipqcfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'me/{0}-{1}/ipqc-{2}{3}'.format(slugify(instance.category.name), instance.version, timezone.now().strftime("%Y%m%d") ,extension)

class Aql(models.Model):
    AQL_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=AQL_OPTIONS,default="")
    version = models.FloatField()
    detail = models.TextField(blank=True)
    aql_file = models.FileField(upload_to=generate_aqlfilename, default="")
    sop_file = models.FileField(upload_to=generate_sopfilename, default="")
    md_file = models.FileField(upload_to=generate_mdfilename, default="")
    bom_file = models.FileField(upload_to=generate_bomfilename, default="")
    ipqc_file = models.FileField(upload_to=generate_ipqcfilename, default="")
    category = models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name="Select Categories")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:aql_list')

    def __str__(self):
        return self.version

 ## 2.7 Order
  ### 2.7.1 Order
class Order(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.PROTECT,verbose_name="Select Supplier",default="")
    user = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="Select User")
    contact = models.ForeignKey(Contact,on_delete=models.PROTECT,verbose_name="Select Supplier Contact")
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    amount = models.FloatField(default="0",blank=True)
    quantity = models.IntegerField(default=0,blank=True)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency",default="", blank=True, null=True)
    deposit_amount = models.FloatField(default="0",blank=True)
    note = models.TextField(blank=True)
    batch_id = models.CharField(max_length=20,default="")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:order_list', kwargs={'pk':self.aql.supplier_id})

    def __str__(self):
        return "Order ID: "+str(self.id)

  ### 2.7.2 OrderProduct
class OrderProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Select Order")
    productprice = models.ForeignKey(ProductPrice,on_delete=models.PROTECT,verbose_name="Select Product",default="")
    quantity = models.IntegerField()
    remaining_quantity = models.IntegerField(blank=True,default=0)
    aql = models.ForeignKey(Aql,on_delete=models.PROTECT,verbose_name="Select AQL",default="")
    paymentterms = models.ForeignKey(PaymentTerms,on_delete=models.PROTECT,verbose_name="Select Payment Terms",default="")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderproduct_list', kwargs={'pk':self.order_id})

    def __str__(self):
        return "Order ID: "+str(self.order_id)

  ### 2.7.3 OrderFile
def generate_orderfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Orders/{1}/order-{2}-{3}-{4}{5}'.format(instance.order.supplier.id, instance.order.id, slugify(instance.order.supplier.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)


class OrderFile(models.Model):
    title = models.CharField(max_length=100)
    file_url = models.FileField(upload_to=generate_orderfilename)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Select Order")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderfile_list', kwargs={'pk':self.order_id})

    def __str__(self):
        return self.title

 ## 2.7.4 OrderDelivery
def generate_orderdeliveryfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Orders/{1}/delivery/delivery-{2}-{3}-{4}{5}'.format(instance.order.supplier.id, instance.order.id, slugify(instance.order.supplier.name), "pi", timezone.now().strftime("%Y%m%d") ,extension)

class OrderDelivery(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT,verbose_name="Select Order")
    quantity = models.IntegerField(blank=True, null=True)
    pi_file = models.FileField(upload_to=generate_orderdeliveryfilename,blank=True)
    date = models.DateTimeField(verbose_name="Select Delivery date",default=timezone.now())
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    batch_id = models.CharField(max_length=20,default="")
    share_percentage = models.FloatField(default="0")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderdelivery_list', kwargs={'pk':self.order_id})

    def __str__(self):
        return self.id

 ## 2.7.5 OrderPayment
def generate_orderpaymentfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Orders/{1}/payments/invoice-{2}-{3}-{4}{5}'.format(instance.order.supplier.id, instance.order.id, slugify(instance.order.supplier.name), slugify(instance.id), timezone.now().strftime("%Y%m%d") ,extension)

class OrderPayment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Select Order")
    bank = models.ForeignKey(Bank,on_delete=models.PROTECT,verbose_name="Select Bank")
    paid_currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Paid Currecy",related_name="paid_currency")
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Invoice Currecy",related_name="invoice_currency")
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    orderdelivery = models.ForeignKey(OrderDelivery,on_delete=models.PROTECT,default="",blank=True,null=True)
    date = models.DateTimeField(verbose_name="Select payment date")
    note = models.TextField(blank=True)
    file_url = models.FileField(upload_to=generate_orderpaymentfilename,blank=True)
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status",default="")
    share_percentage = models.FloatField(default="0")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderpayment_list', kwargs={'pk':self.order_id})

    def __str__(self):
        return "Invoice ID: "+str(self.id)

 ## 2.7.6 OrderDeliveryProduct
def generate_orderdeliveryproductfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Orders/{1}/delivery/delivery-{2}-{3}-{4}{5}'.format(instance.order.supplier.id, instance.order.id, slugify(instance.order.supplier.name), "test-report", timezone.now().strftime("%Y%m%d") ,extension)

class OrderDeliveryProduct(models.Model):
    orderdelivery = models.ForeignKey(OrderDelivery,on_delete=models.PROTECT,verbose_name="Select Order")
    orderproduct = models.ForeignKey(OrderProduct,on_delete=models.PROTECT,verbose_name="Select Order Product")
    quantity = models.IntegerField()
    test_file = models.FileField(upload_to=generate_orderdeliveryproductfilename,blank=True)
    share_percentage = models.FloatField(default="0")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderdeliveryproduct_list', kwargs={'pk':self.orderdelivery_id})

    def __str__(self):
        return self.id

 ## 2.8 Certification
  ### 2.8.1 Certification
def generate_certificationfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'certification/certification-{0}-{1}{2}'.format(slugify(instance.title), timezone.now().strftime("%Y%m%d"), extension)

class Certification(models.Model):
    CERTIFICATION_OPTIONS = (
    ('Active','Active'),
    ('Archived','Archived')
    )
    type = models.CharField(max_length=20,choices=CERTIFICATION_OPTIONS)
    title = models.CharField(max_length=100)
    file_url = models.FileField(upload_to=generate_certificationfilename)
    note = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:certification_list')

    def __str__(self):
        return self.title
