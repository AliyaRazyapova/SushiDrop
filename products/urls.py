from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('products/create/', views.create_product, name='create_product'),
    path('categories/', views.list_categories, name='list_categories'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('nabory/', views.nabory_list, name='nabory_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
