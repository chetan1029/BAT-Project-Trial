from django import forms
from products.models import (Product, PackageMeasurement, ProductBundle, Category, Status,
                            Currency, Size, Color)

# form details
# 1. CategoryForm
# 2. ColorForm
# 3. SizeForm
# 4. StatusForm
# 5. CurrencyForm
# 6. ProductForm
 ## 6.1 ProductForm
 ## 6.2 PackageMeasurementForm
 ## 6.3 ProductBundleForm

# 1. CategoryForm
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name','parent')

# 2. ColorForm
class ColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ('name',)

# 3. SizeForm
class SizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ('name',)

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

# 6. ProductForm
 ## 6.1 ProductForm
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category','title','sku','detail','upc','ean','model_number','size','color','weight','status','image')

 ## 6.2 PackageMeasurementForm
class PackageMeasurementForm(forms.ModelForm):

    class Meta:
        model = PackageMeasurement
        fields = ('title','length','width','depth','weight','unit')

 ## 6.3 ProductBundleForm
class ProductBundleForm(forms.ModelForm):

    class Meta:
        model = ProductBundle
        fields = ('size','color')
