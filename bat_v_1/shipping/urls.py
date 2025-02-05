from django.urls import path
from shipping import views

app_name = "shipping"
urlpatterns = [
    # Shipment
    path('',views.ShipmentListView.as_view(),name='shipment_list'),
    path('ready-to-ship',views.ReadytoshipView.as_view(),name='ready_to_ship'),
    path('add',views.CreateShipmentView.as_view(),name='create_shipment'),
    path('<int:pk>',views.ShipmentDetailView.as_view(),name='shipment_detail'),
    path('<int:pk>/edit/',views.ShipmentUpdateView.as_view(),name='update_shipment'),
    path('<int:pk>/delete/',views.ShipmentDeleteView.as_view(),name='delete_shipment'),
    path('create-shipment',views.create_shipment,name='create_shipment'),
    path('submit-shipment-data',views.submit_shipment_data,name='submit_shipment_data'),
    # Amazon API Calls
    path('<int:pk>/create-amazon-shipment',views.create_amazon_shipment,name='create_amazon_shipment'),
    path('<int:pk>/submit-package-info',views.submit_package_info,name='submit_package_info'),
    # ShipmentProduct
    path('<int:pk>/product',views.ShipmentProductListView.as_view(),name='shipmentproduct_list'),
    path('<int:pk>/product/add',views.CreateShipmentProductView.as_view(),name='create_shipmentproduct'),
    path('product/<int:pk>/edit',views.ShipmentProductUpdateView.as_view(),name='update_shipmentproduct'),
    path('product/<int:pk>/delete',views.ShipmentProductDeleteView.as_view(),name='delete_shipmentproduct'),
    # ShipmentFiles
    path('<int:pk>/files',views.ShipmentFilesListView.as_view(),name='shipmentfiles_list'),
    path('files/<int:pk>/delete',views.ShipmentFilesDeleteView.as_view(),name='delete_shipmentfiles'),
]
