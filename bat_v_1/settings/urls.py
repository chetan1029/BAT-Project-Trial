from django.urls import path
from settings import views

app_name = "settings"
urlpatterns = [
    # Category
    path('category',views.CategoryListView.as_view(),name='category_list'),
    path('category/add',views.CreateCategoryView.as_view(),name='create_category'),
    path('category/<int:pk>/edit/',views.CategoryUpdateView.as_view(),name='update_category'),
    path('category/<int:pk>/delete/',views.CategoryDeleteView.as_view(),name='delete_category'),

    path('ajax/load-display-category',views.load_display_categories,name='ajax_load_display_category'),
    path('ajax/add-category',views.add_category,name='ajax_add_category'),
    # Status
    path('status',views.StatusListView.as_view(),name='status_list'),
    path('status/add',views.CreateStatusView.as_view(),name='create_status'),
    path('status/<int:pk>/edit/',views.StatusUpdateView.as_view(),name='update_status'),
    path('status/<int:pk>/delete/',views.StatusDeleteView.as_view(),name='delete_status'),

    path('ajax/load-display-status',views.load_display_status,name='ajax_load_display_status'),
    path('ajax/add-status',views.add_status,name='ajax_add_status'),
    # Currency
    path('currency',views.CurrencyListView.as_view(),name='currency_list'),
    path('currency/add',views.CreateCurrencyView.as_view(),name='create_currency'),
    path('currency/<int:pk>/edit/',views.CurrencyUpdateView.as_view(),name='update_currency'),
    path('currency/<int:pk>/delete/',views.CurrencyDeleteView.as_view(),name='delete_currency'),
    # AmazonMarket
    path('amazon-market',views.AmazonMarketListView.as_view(),name='amazonmarket_list'),
    path('amazon-market/add',views.CreateAmazonMarketView.as_view(),name='create_amazonmarket'),
    path('amazon-market/<int:pk>/edit/',views.AmazonMarketUpdateView.as_view(),name='update_amazonmarket'),
    path('amazon-market/<int:pk>/delete/',views.AmazonMarketDeleteView.as_view(),name='delete_amazonmarket'),
    path('amazon-market/<int:pk>/sync/',views.sync_amazonmarket,name='sync_amazonmarket'),
    # AmazonMwsauth
    path('amazon-mwsauth',views.AmazonMwsauthListView.as_view(),name='amazonmwsauth_list'),
    path('amazon-mwsauth/add',views.CreateAmazonMwsauthView.as_view(),name='create_amazonmwsauth'),
    path('amazon-mwsauth/<int:pk>/edit/',views.AmazonMwsauthUpdateView.as_view(),name='update_amazonmwsauth'),
    path('amazon-mwsauth/<int:pk>/delete/',views.AmazonMwsauthDeleteView.as_view(),name='delete_amazonmwsauth'),
]
