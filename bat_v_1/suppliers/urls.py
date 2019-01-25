from django.urls import path
from suppliers import views

app_name = "suppliers"
urlpatterns = [
    # Supplier
    path('',views.SupplierListView.as_view(),name='supplier_list'),
    path('add',views.CreateSupplierView.as_view(),name='create_supplier'),
    path('<int:pk>',views.SupplierDetailView.as_view(),name='supplier_detail'),
    path('<int:pk>/edit/',views.SupplierUpdateView.as_view(),name='update_supplier'),
    path('<int:pk>/delete/',views.SupplierDeleteView.as_view(),name='delete_supplier'),
    ## Extra function views for Supplier
    path('ajax/load-display-category',views.load_display_categories,name='ajax_load_display_category'),
    # Payment Terms
    path('payment-terms',views.PaymentTermsListView.as_view(),name='paymentterms_list'),
    path('payment-terms/add',views.CreatePaymentTermsView.as_view(),name='create_paymentterms'),
    path('payment-terms/<int:pk>/edit/',views.PaymentTermsUpdateView.as_view(),name='update_paymentterms'),
    path('payment-terms/<int:pk>/delete/',views.PaymentTermsDeleteView.as_view(),name='delete_paymentterms'),
    # Contact
    path('<int:pk>/contact',views.ContactListView.as_view(),name='contact_list'),
    path('<int:pk>/contact/add',views.CreateContactView.as_view(),name='create_contact'),
    path('contact/<int:pk>/edit/',views.ContactUpdateView.as_view(),name='update_contact'),
    path('contact/<int:pk>/delete/',views.ContactDeleteView.as_view(),name='delete_contact'),
    # Bank
    path('<int:pk>/bank',views.BankListView.as_view(),name='bank_list'),
    path('<int:pk>/bank/add',views.CreateBankView.as_view(),name='create_bank'),
    path('bank/<int:pk>',views.BankDetailView.as_view(),name='bank_detail'),
    path('bank/<int:pk>/edit/',views.BankUpdateView.as_view(),name='update_bank'),
    path('bank/<int:pk>/delete/',views.BankDeleteView.as_view(),name='delete_bank'),
    # Contract
    path('<int:pk>/contract',views.ContractListView.as_view(),name='contract_list'),
    path('<int:pk>/contract/add',views.CreateContractView.as_view(),name='create_contract'),
    path('contract/<int:pk>/edit/',views.ContractUpdateView.as_view(),name='update_contract'),
    path('contract/<int:pk>/delete/',views.ContractDeleteView.as_view(),name='delete_contract'),
    # ProductPrice
    path('<int:pk>/product',views.ProductPriceListView.as_view(),name='productprice_list'),
    path('<int:pk>/product/add',views.CreateProductPriceView.as_view(),name='create_productprice'),
    path('product/<int:pk>/edit/',views.ProductPriceUpdateView.as_view(),name='update_productprice'),
    path('product/<int:pk>/delete/',views.ProductPriceDeleteView.as_view(),name='delete_productprice'),
    # Mold
    path('<int:pk>/mold',views.MoldListView.as_view(),name='mold_list'),
    path('<int:pk>/mold/add',views.CreateMoldView.as_view(),name='create_mold'),
    path('mold/<int:pk>',views.MoldDetailView.as_view(),name='mold_detail'),
    path('mold/<int:pk>/edit/',views.MoldUpdateView.as_view(),name='update_mold'),
    path('mold/<int:pk>/delete/',views.MoldDeleteView.as_view(),name='delete_mold'),
    # MoldFile
    path('mold/<int:pk>/file',views.MoldFileListView.as_view(),name='moldfile_list'),
    path('mold/<int:pk>/file/add',views.CreateMoldFileView.as_view(),name='create_moldfile'),
    path('mold/file/<int:pk>/edit/',views.MoldFileUpdateView.as_view(),name='update_moldfile'),
    path('mold/file/<int:pk>/delete/',views.MoldFileDeleteView.as_view(),name='delete_moldfile'),
    # Aql
    path('<int:pk>/aql',views.AqlListView.as_view(),name='aql_list'),
    path('<int:pk>/aql/add',views.CreateAqlView.as_view(),name='create_aql'),
    path('aql/<int:pk>',views.AqlDetailView.as_view(),name='aql_detail'),
    path('aql/<int:pk>/edit/',views.AqlUpdateView.as_view(),name='update_aql'),
    path('aql/<int:pk>/delete/',views.AqlDeleteView.as_view(),name='delete_aql'),
    # AqlFile
    path('aql/<int:pk>/file',views.AqlFileListView.as_view(),name='aqlfile_list'),
    path('aql/<int:pk>/file/add',views.CreateAqlFileView.as_view(),name='create_aqlfile'),
    path('aql/file/<int:pk>/edit/',views.AqlFileUpdateView.as_view(),name='update_aqlfile'),
    path('aql/file/<int:pk>/delete/',views.AqlFileDeleteView.as_view(),name='delete_aqlfile'),
    # Order
    path('<int:pk>/order',views.OrderListView.as_view(),name='order_list'),
    path('<int:pk>/order/add',views.CreateOrderView.as_view(),name='create_order'),
    path('order/<int:pk>',views.OrderDetailView.as_view(),name='order_detail'),
    path('order/<int:pk>/edit/',views.OrderUpdateView.as_view(),name='update_order'),
    path('order/<int:pk>/delete/',views.OrderDeleteView.as_view(),name='delete_order'),
    # OrderProduct
    path('order/<int:pk>/product',views.OrderProductListView.as_view(),name='orderproduct_list'),
    path('order/<int:pk>/product/add',views.CreateOrderProductView.as_view(),name='create_orderproduct'),
    path('order/product/<int:pk>/edit/',views.OrderProductUpdateView.as_view(),name='update_orderproduct'),
    path('order/product/<int:pk>/delete/',views.OrderProductDeleteView.as_view(),name='delete_orderproduct'),
    # OrderFile
    path('order/<int:pk>/file',views.OrderFileListView.as_view(),name='orderfile_list'),
    path('order/<int:pk>/file/add',views.CreateOrderFileView.as_view(),name='create_orderfile'),
    path('order/file/<int:pk>/edit/',views.OrderFileUpdateView.as_view(),name='update_orderfile'),
    path('order/file/<int:pk>/delete/',views.OrderFileDeleteView.as_view(),name='delete_orderfile'),
    # OrderPayment
    path('order/<int:pk>/payment',views.OrderPaymentListView.as_view(),name='orderpayment_list'),
    path('order/<int:pk>/payment/add',views.CreateOrderPaymentView.as_view(),name='create_orderpayment'),
    path('order/payment/<int:pk>/edit/',views.OrderPaymentUpdateView.as_view(),name='update_orderpayment'),
    path('order/payment/<int:pk>/delete/',views.OrderPaymentDeleteView.as_view(),name='delete_orderpayment'),
    # OrderDelivery
    path('order/<int:pk>/delivery',views.OrderDeliveryListView.as_view(),name='orderdelivery_list'),
    path('order/<int:pk>/delivery/add',views.CreateOrderDeliveryView.as_view(),name='create_orderdelivery'),
    path('order/delivery/<int:pk>/edit/',views.OrderDeliveryUpdateView.as_view(),name='update_orderdelivery'),
    path('order/delivery/<int:pk>/delete/',views.OrderDeliveryDeleteView.as_view(),name='delete_orderdelivery'),
]
