from django.db import models
from django.utils import timezone
from django.urls import reverse
from settings.models import (Category, Status, Currency, AmazonMarket, Box)
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# 1. Product
 ## 1.1 Product
 ## 1.2 PackageMeasurement
 ## 1.3 ProductBundle
# 2. AmazonProduct
 ## 2.1 AmazonProduct

# 1. Product
 ## 1.1 Product
class Product(models.Model):

    title = models.CharField(verbose_name="Product Title", max_length=500)
    image = models.ImageField(upload_to='products/images/',blank=True)
    sku = models.CharField(verbose_name="SKU",max_length=200,blank=True)
    ean = models.CharField(verbose_name="EAN",max_length=200,unique=True)
    model_number = models.CharField(max_length=200,blank=True)
    manufacturer_part_number = models.CharField(max_length=200, default="")
    size = models.CharField(verbose_name="Size",max_length=50,blank=True,default="")
    color = models.CharField(verbose_name="Color",max_length=50,blank=True,default="")
    category = models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name="Select Category")
    bullet_points = models.TextField(blank=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('products:product_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

 ## 1.2 PackageMeasurement
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
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

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

 ## 1.3 ProductBundle
class ProductBundle(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")
    bundle_product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="bundle_product",default="")
    quantity = models.IntegerField(default="1")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('products:productbundle_list', kwargs={'pk':self.product_id})

    def __str__(self):
        return self.product.title

# 2. AmazonProduct
 ## 2.1 AmazonProduct
class AmazonProduct(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="Select Product", blank=True)
    amazonmarket = models.ForeignKey(AmazonMarket,on_delete=models.CASCADE, verbose_name="Select Amazon Marketplace")
    title = models.CharField(verbose_name="Product Title", max_length=500)
    image = models.ImageField(upload_to='products/amazon/images/',blank=True)
    image_url = models.CharField(verbose_name="Image",max_length=500,blank=True)
    seller_sku = models.CharField(verbose_name="Seller SKU",max_length=200,blank=True)
    asin = models.CharField(verbose_name="ASIN",max_length=50)
    packagemeasurement = models.ForeignKey(PackageMeasurement,on_delete=models.PROTECT,verbose_name="Select Package",blank=True)
    box = models.ForeignKey(Box,on_delete=models.PROTECT,verbose_name="Select Box", blank=True)
    units_per_box = models.IntegerField(blank=True)
    total_weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    status = models.ForeignKey(Status,on_delete=models.PROTECT,verbose_name="Select Status")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('products:amazonproduct_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
