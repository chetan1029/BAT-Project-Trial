from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# 1. Basic
 ## 1.1 Category
 ## 1.2 Status
 ## 1.3 Currency
 ## 1.4 Box
# 2. Amazon
 ## 2.1 AmazonMarket
 ## 2.2 AmazonMwsauth
# 3. Company
 ## 3.1 CompanySetting

# 1. Basic
 ## 1.1 Category
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name="children",blank=True,null=True)

    class Meta:
        unique_together = ('name', 'parent')

    def get_absolute_url(self):
        return reverse('settings:category_list')

    def category_breadcrumbs(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' / '.join(full_path[::-1])

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])
    # def __str__(self):
    #     return self.name

 ## 1.2 Status
class Status(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name="children",blank=True,null=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:status_list')

    # def __str__(self):
    #     full_path = [self.title]
    #     k = self.parent
    #
    #     while k is not None:
    #         full_path.append(k.title)
    #         k = k.parent
    #
    #     return ' -> '.join(full_path[::-1])
    def status_breadcrumbs(self):
        full_path = [self.title]
        k = self.parent

        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' / '.join(full_path[::-1])

    def __str__(self):
        return self.title

 ## 1.3 Currency
class Currency(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:currency_list')

    def __str__(self):
        return self.title

# 2. Amazon
 ## 2.1 AmazonMarket
class AmazonMarket(models.Model):
    MARKET_REGION = (
    ('Asia','Asia'),
    ('Europe','Europe'),
    ('North America','North America'),
    ('Oceania','Oceania'),
    ('South America','South America'),
    )

    region = models.CharField(max_length=30,choices=MARKET_REGION,default="Asia",verbose_name="Select Region")
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    domain = models.CharField(max_length=50)
    amazon_id = models.CharField(max_length=10)
    marketplace_id = models.CharField(max_length=50,default="")
    marketplace_image = models.ImageField(upload_to='settings/images/market/',blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:amazonmarket_list')

    def __str__(self):
        return self.name

 ## 2.2 AmazonMwsauth
class AmazonMwsauth(models.Model):
    MARKET_REGION = (
    ('Asia','Asia'),
    ('Europe','Europe'),
    ('North America','North America'),
    ('Oceania','Oceania'),
    ('South America','South America'),
    )

    region = models.CharField(max_length=30,choices=MARKET_REGION,default="Asia",verbose_name="Select Region")
    seller_id = models.CharField(max_length=50,verbose_name="Seller ID")
    auth_token = models.CharField(max_length=100,verbose_name="Auth Token")
    access_key = models.CharField(max_length=100,verbose_name="Access Key")
    secret_key = models.CharField(max_length=100,verbose_name="Secret Key")
    create_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('settings:amazonmwsauth_list')

    def __str__(self):
        return self.region

# 3. Company
 ## 3.1 CompanySetting
class CompanySetting(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='settings/images/',blank=True)
    address1 = models.CharField(max_length=200,verbose_name="Address Line 1")
    address2 = models.CharField(max_length=200,verbose_name="Address Line 2", blank=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=30, verbose_name="Pincode")
    email = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20, verbose_name="Phone Number")
    org_number = models.CharField(max_length=50,default="")
    vat_number = models.CharField(max_length=50,default="")

    def get_formatted_address(self):
        address = ""
        if self.address1 is None and self.address2 is None and self.city is None and self.province is None and self.country is None and self.pincode is None:
            address = ""
        else:
            if self.address1:
                address += self.address1
            if self.address2:
                address += ", "+self.address2
            if self.city:
                address += "<br />"+self.city
            if self.province:
                address += ", "+self.province
            if self.country:
                address += "<br />"+self.country
            if self.pincode:
                address += ", "+self.pincode
        return address.strip(",")

    def __str__(self):
        return self.name
