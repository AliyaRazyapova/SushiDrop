from django.urls import path
from cart import views

urlpatterns = [
    path('get/', views.get_cart_items, name='get_cart_items'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart')
]
