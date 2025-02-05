from django import forms
from suppliers.models import (Supplier, PaymentTerms, Contact, Bank, Contract,
                              ProductPrice, Mold, MoldFile, MoldHost, Aql, Order, OrderProduct, OrderFile,
                              OrderPayment, OrderDelivery, OrderDeliveryProduct, Certification)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
# form details
# 1. PaymentTermsForm
# 2. SupplierForm
 ## 2.1 SupplierForm
 ## 2.2 ContactForm
 ## 2.3 BankForm
 ## 2.4 ContractForm
 ## 2.5 ProductPriceForm
 ## 2.6 MoldForm
  ### 2.6.1 MoldForm
  ### 2.6.2 MoldFileForm
  ### 2.6.3 MoldHostForm
 ## 2.7 AqlForm
  ### 2.7.1 AqlForm
 ## 2.8 OrderForm
  ### 2.8.1 OrderForm
  ### 2.8.2 OrderProductForm
  ### 2.8.3 OrderFileForm
  ### 2.8.4 OrderPaymentForm
  ### 2.8.5 OrderDeliveryForm
 ## 2.9 CertificationForm
  ### 2.9.1 CertificationForm

# 1. PaymentTermsForm
class PaymentTermsForm(forms.ModelForm):

    class Meta:
        model = PaymentTerms
        fields = ('deposit','payment_term','on_delivery')

# 2. SupplierForm
 ## 2.1 SupplierForm
class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('category','name','alternate_name','logo','address1','address2','city','zip','region','region_code','country','country_code','detail')

 ## 2.2 ContactForm
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('type','job_title','first_name','last_name','phone','email','skype','wechat')

 ## 2.3 BankForm
class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = ('type','name','address1','address2','city','zip','region','country','benificary','account_number','swift_code','currency')

 ## 2.4 ContractForm
class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('file_url','note')

 ## 2.5 ProductPriceForm
class ProductPriceForm(forms.ModelForm):

    class Meta:
        model = ProductPrice
        fields = ('product','price','currency')

 ## 2.6 MoldForm
  ### 2.6.1 MoldForm
class MoldForm(forms.ModelForm):

    class Meta:
        model = Mold
        fields = ('title','x_units','price','currency','paid_by','no_of_layers','production_date','category')
        widgets = {
            'production_date': forms.TextInput(attrs={'class': 'datepicker'})
        }

  ### 2.6.2 MoldFileForm
class MoldFileForm(forms.ModelForm):

    class Meta:
        model = MoldFile
        fields = ('file_url','note')

  ### 2.6.2 MoldHostForm
class MoldHostForm(forms.ModelForm):

    class Meta:
        model = MoldHost
        fields = ('supplier','note')

 ## 2.7 AqlForm
   ### 2.7.1 AqlForm
class AqlForm(forms.ModelForm):

    class Meta:
        model = Aql
        fields = ('detail','category','sop_file','md_file','bom_file','ipqc_file','aql_file')

 ## 2.8 OrderForm
  ### 2.8.1 OrderForm
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('note',)

  ### 2.8.2 OrderProductForm
class OrderProductForm(forms.ModelForm):

    class Meta:
        model = OrderProduct
        fields = ('productprice','quantity')

  ### 2.8.3 OrderFileForm
class OrderFileForm(forms.ModelForm):

    class Meta:
        model = OrderFile
        fields = ('title','order','file_url')

  ### 2.8.4 OrderPaymentForm
class OrderPaymentForm(forms.ModelForm):

    class Meta:
        model = OrderPayment
        fields = ('bank','paid_currency','paid_amount','invoice_currency','invoice_amount','date','note','pi_file','receipt_file')
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker'})
        }

  ### 2.8.5 OrderDeliveryForm
class OrderDeliveryForm(forms.ModelForm):

    class Meta:
        model = OrderDelivery
        fields = ('quantity','status')

  ### 2.8.6 OrderDeliveryProductForm
class OrderDeliveryProductForm(forms.ModelForm):

    class Meta:
        model = OrderDeliveryProduct
        fields = ('orderproduct','quantity','status')

 ## 2.8 CertificationForm
  ### 2.8.1 CertificationForm
class CertificationForm(forms.ModelForm):

    class Meta:
        model = Certification
        fields = ('title','file_url','note')
