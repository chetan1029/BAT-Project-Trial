from django.db import models
from django.utils import timezone
from django.urls import reverse
import random
from products.models import Product
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import os, datetime
User = get_user_model()

# Create your models here.
# 1. Main independent models
 ## 1.1 Category
 ## 1.2 Supplier
 ## 1.3 PaymentTerms
 ## 1.4 Status
 ## 1.5 Currency

# 2. Model related with supplier
 ## 2.1 Contact
 ## 2.2 Bank
 ## 2.3 Contract
 ## 2.4 ProductPrice
 ## 2.5 Mold
  ### 2.5.1 Mold
  ### 2.5.2 MoldProduct
  ### 2.5.3 MoldFile
 ## 2.6 Aql
  ### 2.6.1 Aql
  ### 2.6.2 AqlFile

# 1. Main independent models
 ## 1.1 Category
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name="children",blank=True,null=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:category_list')

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

 ## 1.2 Supplier
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
    region = models.CharField(verbose_name="Region/State",max_length=200,blank=True)
    country = models.CharField(max_length=200,blank=True)
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
            if self.country:
                address += ", "+self.country
            if self.zip:
                address += ", "+self.zip
        return address.strip(",")

    def __str__(self):
        return self.name

 ## 1.3 PaymentTerms
class PaymentTerms(models.Model):
    title = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    prepay = models.DecimalField(max_digits=5, decimal_places=2)
    days = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:paymentterms_list')

    def __str__(self):
        return self.title

 ## 1.4 Status
class Status(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:status_list')

    def __str__(self):
        return self.title

 ## 1.5 Currency
class Currency(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:currency_list')

    def __str__(self):
        return self.title

# 2. Model related with supplier
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
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name="Select Currency",default="")
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
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:mold_list', kwargs={'pk':self.supplier_id})

    def __str__(self):
        return self.title

  ### 2.5.2 MoldProduct
class MoldProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT,verbose_name="Select Product")
    mold = models.ForeignKey(Mold,on_delete=models.PROTECT,verbose_name="Select Mold")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:moldproduct_list', kwargs={'pk':self.mold_id})

    def __str__(self):
        return self.product.title

  ### 2.5.3 MoldFile
def generate_moldfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/Molds/mold-{1}-{2}-{3}{4}'.format(instance.mold.supplier.id, slugify(instance.mold.supplier.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)


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
    productprice = models.ForeignKey(ProductPrice,on_delete=models.PROTECT,verbose_name="Select Product")
    version = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:aql_list', kwargs={'pk':self.productprice.supplier_id})

    def __str__(self):
        return self.version

  ### 2.5.2 AqlFile
def generate_aqlfilename(instance, filename):
    name, extension = os.path.splitext(filename)
    return 'suppliers/{0}/AQL/aql-{1}-{2}-{3}{4}'.format(instance.aql.productprice.supplier.id, slugify(instance.aql.productprice.supplier.name), slugify(instance.title), timezone.now().strftime("%Y%m%d") ,extension)


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
