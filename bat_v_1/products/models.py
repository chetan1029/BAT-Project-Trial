from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name="children",blank=True,null=True)

    def get_absolute_url(self):
        return reverse('products:category_detail',kwargs={'pk':self.pk})

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Color(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_STATUS = (
    ('Planning','Planning'),
    ('In Progress','In Progress'),
    ('Final','Final'),
    )

    STATUS_CLASS = {"Planning":"primary", "In Progress":"secondary", "Final":"success"}

    title = models.CharField(verbose_name="Product Title", max_length=500)
    image = models.ImageField(upload_to='products/images/',blank=True)
    sku = models.CharField(verbose_name="SKU",max_length=200,blank=True)
    upc = models.CharField(verbose_name="UPC",max_length=200,blank=True)
    ean = models.CharField(verbose_name="EAN",max_length=200,unique=True)
    model_number = models.CharField(max_length=200,blank=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Select Size")
    color = models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Select Color")
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Select Category")
    detail = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=PRODUCT_STATUS)
    create_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('products:product_detail',kwargs={'pk':self.pk})

    def get_status_class(self):
        status_class_v = "a"
        for status_k in self.STATUS_CLASS:
            print(status_k)
            if status_k == self.status:
                status_class_v = self.STATUS_CLASS[status_k]
        return status_class_v

    def __str__(self):
        return self.title


class PackageMeasurement(models.Model):
    UNIT_TYPE = (
    ('GM-CM','Gm-cm'),
    ('Pound-Inch','Pound-Inch')
    )

    title = models.CharField(verbose_name="Package Title",max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    depth = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=30,choices=UNIT_TYPE)

    def get_absolute_url(self):
        return reverse('products:packagemeasurement_list', kwargs={'pk':self.product_id})

    def get_package_unit(self):
        if self.unit == "GM-CM":
            package_unit = {"length":"cm", "weight":"gm"}
        else:
            package_unit = {"length":"inch", "weight":"pound"}
        return package_unit

    def __str__(self):
        return self.title
