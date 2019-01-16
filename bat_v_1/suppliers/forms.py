from django import forms
from suppliers.models import (Supplier, Category, PaymentTerms, Status, Contact,
                              Currency, Bank, Contract, ProductPrice, Mold,
                              MoldProduct, MoldFile, Aql, AqlFile, AqlProduct,
                              Order, OrderProduct, OrderFile, OrderPayment, OrderDelivery)

# form details
# 1. SupplierForm
# 2. CategoryForm
# 3. PaymentTermsForm
# 4. StatusForm
# 5. CurrencyForm
# 6. ContactForm
# 7. BankForm
# 8. ContractForm
# 9. ProductPriceForm
# 10. MoldForm
# 11. MoldProductForm
# 12. MoldFileForm
# 13. AqlForm
# 14. AqlFileForm
# 15. AqlProductForm
# 16. OrderForm
# 17. OrderProductForm
# 18. OrderFileForm
# 19. OrderPaymentForm
# 20. OrderDeliveryForm

# 1. SupplierForm
class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('category','name','alternate_name','logo','address1','address2','city','zip','region','country','detail')

# 2. CategoryForm
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name','parent')

# 3. PaymentTermsForm
class PaymentTermsForm(forms.ModelForm):

    class Meta:
        model = PaymentTerms
        fields = ('title','identifier','prepay','days')

# 4. StatusForm
class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('title','parent')

# 5. CurrencyForm
class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('title',)

# 6. ContactForm
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone','email','skype','wechat')

# 7. BankForm
class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = ('name','address1','address2','city','zip','region','country','benificary','account_number','swift_number','swift_code','currency')

# 8. ContractForm
class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('title','file_url')

# 9. ProductPriceForm
class ProductPriceForm(forms.ModelForm):

    class Meta:
        model = ProductPrice
        fields = ('product','price','currency','version','status')

# 10. MoldForm
class MoldForm(forms.ModelForm):

    class Meta:
        model = Mold
        fields = ('title','mold_supplier','x_units','price','currency','paid_by','no_of_layers','production_date')
        widgets = {
            'paid_by': forms.RadioSelect(),
            'production_date': forms.TextInput(attrs={'class': 'datepicker'})
        }

# 11. MoldProductForm
class MoldProductForm(forms.ModelForm):

    class Meta:
        model = MoldProduct
        fields = ('product',)

# 12. MoldFileForm
class MoldFileForm(forms.ModelForm):

    class Meta:
        model = MoldFile
        fields = ('title','file_url','note')

# 13. AqlForm
class AqlForm(forms.ModelForm):

    class Meta:
        model = Aql
        fields = ('version','detail')


# 14. AqlFileForm
class AqlFileForm(forms.ModelForm):

    class Meta:
        model = AqlFile
        fields = ('title','file_url')

# 15. AqlProductForm
class AqlProductForm(forms.ModelForm):

    class Meta:
        model = AqlProduct
        fields = ('product',)

# 16. OrderForm
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('aql','user','contact','paymentterms','status','note')

# 17. OrderProductForm
class OrderProductForm(forms.ModelForm):

    class Meta:
        model = OrderProduct
        fields = ('product','price','currency','quantity')

# 18. OrderFileForm
class OrderFileForm(forms.ModelForm):

    class Meta:
        model = OrderFile
        fields = ('title','file_url')

# 19. OrderPaymentForm
class OrderPaymentForm(forms.ModelForm):

    class Meta:
        model = OrderPayment
        fields = ('bank','paid_currency','paid_amount','invoice_currency','invoice_amount','date','note','file_url')
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker'})
        }

# 20. OrderDeliveryForm
class OrderDeliveryForm(forms.ModelForm):

    class Meta:
        model = OrderDelivery
        fields = ('title','quantity','orderpayment','status','file_url')
