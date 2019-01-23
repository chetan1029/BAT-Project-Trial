from django.urls import path
from shipping import views

app_name = "shipping"
urlpatterns = [
    # Shipment
    path('',views.ShipmentListView.as_view(),name='shipment_list'),
    path('add',views.CreateShipmentView.as_view(),name='create_shipment'),
    path('<int:pk>',views.ShipmentDetailView.as_view(),name='shipment_detail'),
    path('<int:pk>/edit/',views.ShipmentUpdateView.as_view(),name='update_shipment'),
    path('<int:pk>/delete/',views.ShipmentDeleteView.as_view(),name='delete_shipment'),
    # Amazon API Calls
    path('<int:pk>/create-amazon-shipment',views.create_amazon_shipment,name='create_amazon_shipment'),
    # ShipmentProduct
    path('<int:pk>/product',views.ShipmentProductListView.as_view(),name='shipmentproduct_list'),
    path('<int:pk>/product/add',views.CreateShipmentProductView.as_view(),name='create_shipmentproduct'),
    path('product/<int:pk>/edit',views.ShipmentProductUpdateView.as_view(),name='update_shipmentproduct'),
    path('product/<int:pk>/delete',views.ShipmentProductDeleteView.as_view(),name='delete_shipmentproduct'),
]
