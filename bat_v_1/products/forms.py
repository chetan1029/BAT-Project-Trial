from django import forms
from products.models import Product, PackageMeasurement

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category','title','sku','detail','upc','ean','model_number','size','color','weight','status')

class PackageMeasurementForm(forms.ModelForm):

    class Meta:
        model = PackageMeasurement
        fields = ('product','title','length','width','depth','weight','unit')
