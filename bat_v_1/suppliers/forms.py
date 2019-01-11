from django import forms
from suppliers.models import (Supplier, Category, PaymentTerms, Status, Contact,
                              Currency, Bank, Contract, ProductPrice, Mold, MoldProduct)

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
        fields = ('title',)

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
