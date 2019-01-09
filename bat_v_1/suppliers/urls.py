from django.urls import path
from suppliers import views

app_name = "suppliers"
urlpatterns = [
    path('',views.SupplierListView.as_view(),name='supplier_list'),
    path('add',views.CreateSupplierView.as_view(),name='create_supplier'),
    path('<int:pk>',views.SupplierDetailView.as_view(),name='supplier_detail'),
    path('<int:pk>/edit/',views.SupplierUpdateView.as_view(),name='update_supplier'),
    path('<int:pk>/delete/',views.SupplierDeleteView.as_view(),name='delete_supplier'),
    path('category',views.CategoryListView.as_view(),name='category_list'),
    path('category/add',views.CreateCategoryView.as_view(),name='create_category'),
    path('category/<int:pk>/edit/',views.CategoryUpdateView.as_view(),name='update_category'),
    path('category/<int:pk>/delete/',views.CategoryDeleteView.as_view(),name='delete_category'),
    path('payment-terms',views.PaymentTermsListView.as_view(),name='paymentterms_list'),
    path('payment-terms/add',views.CreatePaymentTermsView.as_view(),name='create_paymentterms'),
    path('payment-terms/<int:pk>/edit/',views.PaymentTermsUpdateView.as_view(),name='update_paymentterms'),
    path('payment-terms/<int:pk>/delete/',views.PaymentTermsDeleteView.as_view(),name='delete_paymentterms'),
    path('status',views.StatusListView.as_view(),name='status_list'),
    path('status/add',views.CreateStatusView.as_view(),name='create_status'),
    path('status/<int:pk>/edit/',views.StatusUpdateView.as_view(),name='update_status'),
    path('status/<int:pk>/delete/',views.StatusDeleteView.as_view(),name='delete_status'),
]
