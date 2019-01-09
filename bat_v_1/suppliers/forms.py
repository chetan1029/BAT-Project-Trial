from django import forms
from suppliers.models import Supplier, Category, PaymentTerms, Status

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('category','name','alternate_name','logo','address1','address2','city','zip','region','country','detail')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name','parent')

class PaymentTermsForm(forms.ModelForm):

    class Meta:
        model = PaymentTerms
        fields = ('title','identifier','prepay','days')

class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('title',)
