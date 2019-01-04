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

    title = models.CharField(max_length=500)
    sku = models.CharField(max_length=200,blank=True)
    upc = models.CharField(max_length=200,blank=True)
    ean = models.CharField(max_length=200,unique=True)
    model_number = models.CharField(max_length=200,blank=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    detail = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=PRODUCT_STATUS)
    create_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('products:product_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class PackageMeasurement(models.Model):
    UNIT_TYPE = (
    ('GM-CM','Gm-cm'),
    ('Pound-Inch','Pound-Inch')
    )

    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    depth = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=30,choices=UNIT_TYPE)

    def get_absolute_url(self):
        return reverse('products:packagemeasurement_list')

    def __str__(self):
        return self.title
