from django.urls import path
from . import views

urlpatterns = [
    path('products/create/', views.create_product, name='create_product'),
    path('categories/', views.list_categories, name='list_categories'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]
