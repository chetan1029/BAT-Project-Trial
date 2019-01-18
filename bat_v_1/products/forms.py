from django import forms
from products.models import (Product, PackageMeasurement, ProductBundle, AmazonProduct)

# form details
# 1. ProductForm
 ## 1.1 ProductForm
 ## 1.2 PackageMeasurementForm
 ## 1.3 ProductBundleForm
# 2. AmazonProductForm
 ## 2.1 AmazonProductForm

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

# 2. AmazonProductForm
 ## 2.1 AmazonProductForm
class AmazonProductForm(forms.ModelForm):

    class Meta:
        model = AmazonProduct
        fields = ('product','amazonmarket','title','seller_sku','asin','packagemeasurement','box','units_per_box','total_weight','status','image')
