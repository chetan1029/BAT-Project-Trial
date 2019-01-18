from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# 1. Basic
 ## 1.1 Category
 ## 1.2 Color
 ## 1.3 Size
 ## 1.4 Status
 ## 1.5 Currency
 ## 1.6 Box
# 2. Amazon
 ## 2.1 AmazonMarket

# 1. Basic
 ## 1.1 Category
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name="children",blank=True,null=True)

    class Meta:
        unique_together = ('name', 'parent')

    def get_absolute_url(self):
        return reverse('settings:category_list')

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

 ## 1.2 Color
class Color(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def get_absolute_url(self):
        return reverse('settings:color_list')

    def __str__(self):
        return self.name

 ## 1.3 Size
class Size(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def get_absolute_url(self):
        return reverse('settings:size_list')

    def __str__(self):
        return self.name

 ## 1.4 Status
class Status(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name="children",blank=True,null=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:status_list')

    def __str__(self):
        full_path = [self.title]
        k = self.parent

        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' -> '.join(full_path[::-1])

 ## 1.5 Currency
class Currency(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:currency_list')

    def __str__(self):
        return self.title

 ## 1.6 Box
class Box(models.Model):
    title = models.CharField(max_length=200)
    length = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Length (cm)")
    width = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Width (cm)")
    depth = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Depth (cm)")
    cbm = models.DecimalField(max_digits=7, decimal_places=3, verbose_name="CBM")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:box_list')

    def __str__(self):
        return self.title

# 2. Amazon
 ## 2.1 AmazonMarket
class AmazonMarket(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    domain = models.CharField(max_length=50)
    amazon_id = models.CharField(max_length=10)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:amazonmarket_list')

    def __str__(self):
        return self.name
