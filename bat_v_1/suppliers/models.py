from django.db import models
from django.utils import timezone
from django.urls import reverse
import random
from products.models import (Product)
from settings.models import (Category, Status, Currency)
from django.contrib.auth import get_user_model
from django.utils.text import slugify
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
  ### 2.6.2 AqlFile
 ## 2.7 Order
  ### 2.7.1 Order
  ### 2.7.2 OrderProduct
  ### 2.7.3 OrderFile
  ### 2.7.4 OrderPayment
  ### 2.7.5 OrderDelivery

# 1. PaymentTerms
class PaymentTerms(models.Model):
    title = models.CharField(max_length=200)
    prepay = models.DecimalField(max_digits=5, decimal_places=2)
    days = models.IntegerField()
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
                address += ", "+self.city
            if self.region:
                address += ", "+self.region
            if self.region_code:
                address += " ("+self.region_code+")"
            if self.country:
                address += ", "+self.country
            if self.country_code:
                address += " ("+self.country_code+")"
            if self.zip:
                address += ", "+self.zip
        return address.strip(",")

    def __str__(self):
        return self.name

 ## 2.1 Contact
class Contact(models.Model):
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
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200)
    zip = models.CharField(verbose_name="Zip/Pin Code",max_length=200)
    region = models.CharField(verbose_name="Region/State",max_length=200,blank=True)
    country = models.CharField(max_length=200)
    benificary = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    swift_number = models.CharField(max_length=50)
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
    title = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name="Select Supplier")
    file_url = models.FileField(upload_to=generate_filename)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:contract_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.title

 ## 2.4 ProductPrice
class ProductPrice(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name="Select Supplier")
    product = models.ForeignKey(Product,on_delete=models.PROTECT,verbose_name="Select Product")
    price = models.DecimalField(max_digits=7, decimal_places=3)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency")
    version = models.CharField(max_length=50)
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:productprice_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.product.title

 ## 2.5 Mold
  ### 2.5.1 Mold
class Mold(models.Model):
    PAID_BY_OPTIONS = (
    ('Supplier','Supplier'),
    ('Us','Us')
    )

    title = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier,on_delete=models.PROTECT,verbose_name="Select Supplier")
    mold_supplier = models.ForeignKey(Supplier,on_delete=models.PROTECT,verbose_name="Select Mold Supplier",related_name="mold_supplier")
    x_units = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=3)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency")
    no_of_layers = models.IntegerField()
    paid_by = models.CharField(max_length=20,choices=PAID_BY_OPTIONS,default="")
    production_date = models.DateField()
    product = models.ManyToManyField(Product,verbose_name="Select Products")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:mold_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.title

  ### 2.5.2 MoldFile
def generate_moldfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Molds/{1}/mold-{2}-{3}-{4}{5}'.format(instance.mold.supplier.id, instance.mold.id, slugify(instance.mold.supplier.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)


class MoldFile(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    file_url = models.FileField(upload_to=generate_moldfilename)
    mold = models.ForeignKey(Mold,on_delete=models.PROTECT,verbose_name="Select Mold")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:moldfile_list', kwargs={'pk':self.mold_id})

    def __str__(self):
        return self.title

 ## 2.6 Aql
  ### 2.6.1 Aql
class Aql(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.PROTECT,verbose_name="Select Supplier",default=1)
    version = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    product = models.ManyToManyField(Product,verbose_name="Select Products")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:aql_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.version

  ### 2.6.2 AqlFile
def generate_aqlfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/AQL/{1}/aql-{2}-{3}-{4}{5}'.format(instance.aql.supplier.id, instance.aql.id, slugify(instance.aql.supplier.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)


class AqlFile(models.Model):
    title = models.CharField(max_length=100)
    file_url = models.FileField(upload_to=generate_aqlfilename)
    aql = models.ForeignKey(Aql,on_delete=models.PROTECT,verbose_name="Select AQL")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:aqlfile_list', kwargs={'pk':self.aql_id})

    def __str__(self):
        return self.title


 ## 2.7 Order
  ### 2.7.1 Order
class Order(models.Model):
    aql = models.ForeignKey(Aql,on_delete=models.PROTECT,verbose_name="Select AQL")
    user = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="Select User")
    contact = models.ForeignKey(Contact,on_delete=models.PROTECT,verbose_name="Select Supplier Contact")
    paymentterms = models.ForeignKey(PaymentTerms,on_delete=models.PROTECT,verbose_name="Select Payment Terms")
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    note = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:order_list', kwargs={'pk':self.aql.supplier_id})

    def __str__(self):
        return "Order ID: "+str(self.id)

  ### 2.7.2 OrderProduct
class OrderProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Select Order")
    product = models.ForeignKey(Product,on_delete=models.PROTECT,verbose_name="Select Product")
    price = models.DecimalField(max_digits=7, decimal_places=3)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency")
    quantity = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderproduct_list', kwargs={'pk':self.order_id})

    def __str__(self):
        return "Order ID: "+str(self.order_id)+", Product: "+self.product.title

  ### 2.7.3 OrderFile
def generate_orderfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Orders/{1}/order-{2}-{3}-{4}{5}'.format(instance.order.aql.supplier.id, instance.order.id, slugify(instance.order.aql.supplier.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)


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

 ## 2.7.4 OrderPayment
def generate_orderpaymentfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Orders/{1}/payments/invoice-{2}-{3}-{4}{5}'.format(instance.order.aql.supplier.id, instance.order.id, slugify(instance.order.aql.supplier.name), slugify(instance.id), timezone.now().strftime("%Y%m%d") ,extension)

class OrderPayment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Select Order")
    bank = models.ForeignKey(Bank,on_delete=models.PROTECT,verbose_name="Select Bank")
    paid_currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Paid Currecy",related_name="paid_currency")
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Invoice Currecy",related_name="invoice_currency")
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(verbose_name="Select payment date")
    note = models.TextField(blank=True)
    file_url = models.FileField(upload_to=generate_orderpaymentfilename)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderpayment_list', kwargs={'pk':self.order_id})

    def __str__(self):
        return "Invoice ID: "+str(self.id)

 ## 2.7.5 OrderDelivery
def generate_orderdeliveryfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Orders/{1}/delivery/delivery-{2}-{3}-{4}{5}'.format(instance.order.aql.supplier.id, instance.order.id, slugify(instance.order.aql.supplier.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)

class OrderDelivery(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Select Order")
    title = models.CharField(max_length=100)
    orderproduct = models.ForeignKey(OrderProduct,on_delete=models.CASCADE,verbose_name="Select Order Product", default="")
    quantity = models.IntegerField()
    orderpayment = models.ForeignKey(OrderPayment,on_delete=models.CASCADE,verbose_name="Select Order Payment")
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    file_url = models.FileField(upload_to=generate_orderdeliveryfilename,blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:orderdelivery_list', kwargs={'pk':self.order_id})

    def __str__(self):
        return self.title
