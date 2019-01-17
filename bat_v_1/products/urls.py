from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    # Category
    path('category',views.CategoryListView.as_view(),name='category_list'),
    path('category/add',views.CreateCategoryView.as_view(),name='create_category'),
    path('category/<int:pk>/edit/',views.CategoryUpdateView.as_view(),name='update_category'),
    path('category/<int:pk>/delete/',views.CategoryDeleteView.as_view(),name='delete_category'),
    # Status
    path('status',views.StatusListView.as_view(),name='status_list'),
    path('status/add',views.CreateStatusView.as_view(),name='create_status'),
    path('status/<int:pk>/edit/',views.StatusUpdateView.as_view(),name='update_status'),
    path('status/<int:pk>/delete/',views.StatusDeleteView.as_view(),name='delete_status'),
    # Currency
    path('currency',views.CurrencyListView.as_view(),name='currency_list'),
    path('currency/add',views.CreateCurrencyView.as_view(),name='create_currency'),
    path('currency/<int:pk>/edit/',views.CurrencyUpdateView.as_view(),name='update_currency'),
    path('currency/<int:pk>/delete/',views.CurrencyDeleteView.as_view(),name='delete_currency'),
    # Color
    path('color',views.ColorListView.as_view(),name='color_list'),
    path('color/add',views.CreateColorView.as_view(),name='create_color'),
    path('color/<int:pk>/edit/',views.ColorUpdateView.as_view(),name='update_color'),
    path('color/<int:pk>/delete/',views.ColorDeleteView.as_view(),name='delete_color'),
    # Size
    path('size',views.SizeListView.as_view(),name='size_list'),
    path('size/add',views.CreateSizeView.as_view(),name='create_size'),
    path('size/<int:pk>/edit/',views.SizeUpdateView.as_view(),name='update_size'),
    path('size/<int:pk>/delete/',views.SizeDeleteView.as_view(),name='delete_size'),
    # Product
    path('',views.ProductListView.as_view(),name='product_list'),
    path('add',views.CreateProductView.as_view(),name='create_product'),
    path('<int:pk>',views.ProductDetailView.as_view(),name='product_detail'),
    path('<int:pk>/edit/',views.ProductUpdateView.as_view(),name='update_product'),
    path('<int:pk>/delete/',views.ProductDeleteView.as_view(),name='delete_product'),
    # PackageMeasurement
    path('<int:pk>/package-measurement',views.PackageMeasurementListView.as_view(),name='packagemeasurement_list'),
    path('<int:pk>/package-measurement/add',views.CreatePackageMeasurementView.as_view(),name='create_packagemeasurement'),
    path('package-measurement/<int:pk>/edit',views.PackageMeasurementUpdateView.as_view(),name='update_packagemeasurement'),
    path('package-measurement/<int:pk>/delete',views.PackageMeasurementDeleteView.as_view(),name='delete_packagemeasurement'),
    # ProductBundle
    path('<int:pk>/product-bundle',views.ProductBundleListView.as_view(),name='productbundle_list'),
    path('<int:pk>/product-bundle/add',views.CreateProductBundleView.as_view(),name='create_productbundle'),
    path('product-bundle/<int:pk>/edit',views.ProductBundleUpdateView.as_view(),name='update_productbundle'),
    path('product-bundle/<int:pk>/delete',views.ProductBundleDeleteView.as_view(),name='delete_productbundle'),
]
