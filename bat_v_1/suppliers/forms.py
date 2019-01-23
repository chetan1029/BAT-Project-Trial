from django import forms
from suppliers.models import (Supplier, PaymentTerms, Contact, Bank, Contract,
                              ProductPrice, Mold, MoldProduct, MoldFile, Aql,
                              AqlFile, AqlProduct, Order, OrderProduct, OrderFile,
                              OrderPayment, OrderDelivery)

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
  ### 2.6.2 MoldProductForm
  ### 2.6.3 MoldFileForm
 ## 2.7 AqlForm
  ### 2.7.1 AqlForm
  ### 2.7.2 AqlFileForm
  ### 2.7.3 AqlProductForm
 ## 2.8 OrderForm
  ### 2.8.1 OrderForm
  ### 2.8.2 OrderProductForm
  ### 2.8.3 OrderFileForm
  ### 2.8.4 OrderPaymentForm
  ### 2.8.5 OrderDeliveryForm

# 1. PaymentTermsForm
class PaymentTermsForm(forms.ModelForm):

    class Meta:
        model = PaymentTerms
        fields = ('title','identifier','prepay','days')

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
        fields = ('first_name','last_name','phone','email','skype','wechat')

 ## 2.3 BankForm
class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = ('name','address1','address2','city','zip','region','country','benificary','account_number','swift_number','swift_code','currency')

 ## 2.4 ContractForm
class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('title','file_url')

 ## 2.5 ProductPriceForm
class ProductPriceForm(forms.ModelForm):

    class Meta:
        model = ProductPrice
        fields = ('product','price','currency','version','status')

 ## 2.6 MoldForm
  ### 2.6.1 MoldForm
class MoldForm(forms.ModelForm):

    class Meta:
        model = Mold
        fields = ('title','mold_supplier','x_units','price','currency','paid_by','no_of_layers','production_date')
        widgets = {
            'paid_by': forms.RadioSelect(),
            'production_date': forms.TextInput(attrs={'class': 'datepicker'})
        }

  ### 2.6.2 MoldProductForm
class MoldProductForm(forms.ModelForm):

    class Meta:
        model = MoldProduct
        fields = ('product',)

  ### 2.6.3 MoldFileForm
class MoldFileForm(forms.ModelForm):

    class Meta:
        model = MoldFile
        fields = ('title','file_url','note')

 ## 2.7 AqlForm
   ### 2.7.1 AqlForm
class AqlForm(forms.ModelForm):

    class Meta:
        model = Aql
        fields = ('version','detail')


  ### 2.7.2 AqlFileForm
class AqlFileForm(forms.ModelForm):

    class Meta:
        model = AqlFile
        fields = ('title','file_url')

  ### 2.7.3 AqlProductForm
class AqlProductForm(forms.ModelForm):

    class Meta:
        model = AqlProduct
        fields = ('product',)

 ## 2.8 OrderForm
  ### 2.8.1 OrderForm
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('aql','user','contact','paymentterms','status','note')

  ### 2.8.2 OrderProductForm
class OrderProductForm(forms.ModelForm):

    class Meta:
        model = OrderProduct
        fields = ('product','price','currency','quantity')

  ### 2.8.3 OrderFileForm
class OrderFileForm(forms.ModelForm):

    class Meta:
        model = OrderFile
        fields = ('title','file_url')

  ### 2.8.4 OrderPaymentForm
class OrderPaymentForm(forms.ModelForm):

    class Meta:
        model = OrderPayment
        fields = ('bank','paid_currency','paid_amount','invoice_currency','invoice_amount','date','note','file_url')
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker'})
        }

  ### 2.8.5 OrderDeliveryForm
class OrderDeliveryForm(forms.ModelForm):

    class Meta:
        model = OrderDelivery
        fields = ('title','orderproduct','quantity','orderpayment','status','file_url')
