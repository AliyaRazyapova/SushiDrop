from django.urls import path
from . import views

urlpatterns = [
    path('products/create/', views.create_product, name='create_product'),
    path('categories/', views.list_categories, name='list_categories')
]
