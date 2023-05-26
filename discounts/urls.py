from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiscountView.as_view(), name='discounts'),
    path('list/', views.DiscountListView.as_view(), name='discounts_list'),
    path('add/', views.DiscountCreateView.as_view(), name='create_discounts'),
    path('<int:discount_id>/', views.DiscountUpdateView.as_view(), name='edit_discounts')
]
