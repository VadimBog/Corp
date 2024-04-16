from django.urls import path
from .views import cart_view, cart_add, cart_delete, cart_update

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart-view'),
    path('add/', cart_add, name='add_to_cart'),
    path('delete/', cart_delete, name='delete_to_cart'),
    path('update/', cart_update, name='update_to_cart'),
]