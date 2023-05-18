from django.urls import path
from cart.views import get_cart_items

urlpatterns = [
    path('get/', get_cart_items, name='get_cart_items')
]
