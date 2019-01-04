from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    path('',views.ProductListView.as_view(),name='product_list'),
    path('add',views.CreateProductView.as_view(),name='create_product'),
    path('<int:pk>',views.ProductDetailView.as_view(),name='product_detail'),
    path('<int:pk>/edit/',views.ProductUpdateView.as_view(),name='update_product'),
    path('<int:pk>/delete/',views.ProductDeleteView.as_view(),name='delete_product'),
]
