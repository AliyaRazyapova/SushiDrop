from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiscountView.as_view(), name='discounts'),
    path('add/', views.DiscountCreateView.as_view(), name='create_discounts')
]
