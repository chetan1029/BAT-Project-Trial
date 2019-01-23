from django import forms
from settings.models import (Category, Status, Currency, Size, Color,
                             AmazonMarket, AmazonMwsauth, Box)

# form details
# 1. Basic
 ## 1.1 CategoryForm
 ## 1.2 ColorForm
 ## 1.3 SizeForm
 ## 1.4 StatusForm
 ## 1.5 CurrencyForm
 ## 1.6 BoxForm
# 2. Amazon
 ## 2.1 AmazonMarketForm
 ## 2.2 AmazonMwsauthForm

# 1. Basic
 ## 1.1 CategoryForm
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name','parent')

 ## 1.2 ColorForm
class ColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ('name',)

 ## 1.3 SizeForm
class SizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ('name',)

 ## 1.4 StatusForm
class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('title','parent')

 ## 1.5 CurrencyForm
class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('title',)

 ## 1.6 BoxForm
class BoxForm(forms.ModelForm):

    class Meta:
        model = Box
        fields = ('title','length','width','depth')

# 2. Amazon
 ## 2.1 AmazonMarketForm
class AmazonMarketForm(forms.ModelForm):

    class Meta:
        model = AmazonMarket
        fields = ('identifier','name','country_code','domain','amazon_id','marketplace_id')

 ## 2.2 AmazonMwsauthForm
class AmazonMwsauthForm(forms.ModelForm):

    class Meta:
        model = AmazonMwsauth
        fields = ('identifier','seller_id','auth_token','access_key','secret_key')
