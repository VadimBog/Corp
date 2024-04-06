from django.urls import path
from .views import products_view, categories_list, product_detail_view

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products'),
    path('<slug:slug>/', product_detail_view, name='product-detail'),
    path('search/<slug:slug>/', categories_list, name='category-list'),
]