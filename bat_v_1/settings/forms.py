from django import forms
from settings.models import (Category, Status, Currency,
                             AmazonMarket, AmazonMwsauth, CompanySetting)

# form details
# 1. Basic
 ## 1.1 CategoryForm
 ## 1.2 StatusForm
 ## 1.3 CurrencyForm
 ## 1.4 BoxForm
# 2. Amazon
 ## 2.1 AmazonMarketForm
 ## 2.2 AmazonMwsauthForm
# 3. Company
 ## 3.1 CompanySettingForm

# 1. Basic
 ## 1.1 CategoryForm
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name','parent')

 ## 1.2 StatusForm
class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('title','parent')

 ## 1.3 CurrencyForm
class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('title',)

# 2. Amazon
 ## 2.1 AmazonMarketForm
class AmazonMarketForm(forms.ModelForm):

    class Meta:
        model = AmazonMarket
        fields = ('region','name','country_code','domain','amazon_id','marketplace_id','marketplace_image')

 ## 2.2 AmazonMwsauthForm
class AmazonMwsauthForm(forms.ModelForm):

    class Meta:
        model = AmazonMwsauth
        fields = ('region','seller_id','auth_token','access_key','secret_key')

# 3. Company
 ## 3.1 CompanySettingForm
class CompanySettingForm(forms.ModelForm):

    class Meta:
        model = CompanySetting
        fields = ('name','image','address1','address2','city','province','country','pincode','email','phonenumber','org_number','vat_number')
