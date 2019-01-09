from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# 1. Category
# 2. Supplier
# 3. PaymentTerms
# 4. Status

# 1. Category
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

# 2. Supplier
class Supplier(models.Model):

    name = models.CharField(verbose_name="Supplier Name", max_length=200)
    alternate_name = models.CharField(verbose_name="Supplier Alternative Name", max_length=200,blank=True)
    logo = models.ImageField(upload_to='suppliers/logo/',blank=True)
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
        return address

    def __str__(self):
        return self.title

# 3. PaymentTerms
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

# 4. Status
class Status(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('suppliers:status_list')

    def __str__(self):
        return self.title
