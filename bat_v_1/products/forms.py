from django import forms
from products.models import (Product, PackageMeasurement, ProductBundle)

# form details
# 1. ProductForm
 ## 1.1 ProductForm
 ## 1.2 PackageMeasurementForm
 ## 1.3 ProductBundleForm

# 1. ProductForm
 ## 1.1 ProductForm
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category','title','sku','detail','upc','ean','model_number','size','color','weight','status','image')

 ## 1.2 PackageMeasurementForm
class PackageMeasurementForm(forms.ModelForm):

    class Meta:
        model = PackageMeasurement
        fields = ('title','length','width','depth','weight','unit')

 ## 1.3 ProductBundleForm
class ProductBundleForm(forms.ModelForm):

    class Meta:
        model = ProductBundle
        fields = ('size','color')
