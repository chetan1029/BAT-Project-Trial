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
]
