from django import forms
from products.models import (Product, PackageMeasurement, ProductBundle, AmazonProduct)
from settings.models import (Status)
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
        fields = ('category','title','sku','ean','color','size','model_number','manufacturer_part_number','bullet_points','description','status','image')
        widgets = {
            'category': forms.Select(attrs = {'onchange' : "load_categories(this.value);"}),
            'bullet_points': forms.Textarea(attrs={'class': 'ckEditorClassic'}),
            'description': forms.Textarea(attrs={'class': 'ckEditorClassic'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Products'))

 ## 1.2 PackageMeasurementForm
class PackageMeasurementForm(forms.ModelForm):

    class Meta:
        model = PackageMeasurement
        fields = ('title','length','width','depth','weight','unit')

 ## 1.3 ProductBundleForm
class ProductBundleForm(forms.ModelForm):

    class Meta:
        model = ProductBundle
        fields = ('bundle_product','quantity')

ProductBundleFormSet = forms.inlineformset_factory(Product, ProductBundle, fk_name="product", form=ProductBundleForm, extra=1)

# 2. AmazonProductForm
 ## 2.1 AmazonProductForm
class AmazonProductForm(forms.ModelForm):

    class Meta:
        model = AmazonProduct
        fields = ('product','amazonmarket','title','seller_sku','asin','packagemeasurement','box','units_per_box','total_weight','status','image')
