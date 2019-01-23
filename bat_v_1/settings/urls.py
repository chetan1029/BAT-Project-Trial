from django.urls import path
from settings import views

app_name = "settings"
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
    # AmazonMarket
    path('amazon-market',views.AmazonMarketListView.as_view(),name='amazonmarket_list'),
    path('amazon-market/add',views.CreateAmazonMarketView.as_view(),name='create_amazonmarket'),
    path('amazon-market/<int:pk>/edit/',views.AmazonMarketUpdateView.as_view(),name='update_amazonmarket'),
    path('amazon-market/<int:pk>/delete/',views.AmazonMarketDeleteView.as_view(),name='delete_amazonmarket'),
    # Box
    path('box',views.BoxListView.as_view(),name='box_list'),
    path('box/add',views.CreateBoxView.as_view(),name='create_box'),
    path('box/<int:pk>/edit/',views.BoxUpdateView.as_view(),name='update_box'),
    path('box/<int:pk>/delete/',views.BoxDeleteView.as_view(),name='delete_box'),
    # AmazonMwsauth
    path('amazon-mwsauth',views.AmazonMwsauthListView.as_view(),name='amazonmwsauth_list'),
    path('amazon-mwsauth/add',views.CreateAmazonMwsauthView.as_view(),name='create_amazonmwsauth'),
    path('amazon-mwsauth/<int:pk>/edit/',views.AmazonMwsauthUpdateView.as_view(),name='update_amazonmwsauth'),
    path('amazon-mwsauth/<int:pk>/delete/',views.AmazonMwsauthDeleteView.as_view(),name='delete_amazonmwsauth'),
]
