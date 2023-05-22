from django.urls import path
from .views import DiscountView

urlpatterns = [
    path('', DiscountView.as_view(), name='discounts'),
]
