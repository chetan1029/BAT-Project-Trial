from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
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
