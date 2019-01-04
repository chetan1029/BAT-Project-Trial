from django.contrib import admin
from products.models import Product, Color, Size, Category, PackageMeasurement
# Register your models here.

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(PackageMeasurement)
