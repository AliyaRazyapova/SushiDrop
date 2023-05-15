from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('products/create/', views.create_product, name='create_product'),
    path('categories/', views.list_categories, name='list_categories'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/nabory/', views.product_list, {'category_id': 1}, name='nabory_list'),
    path('products/premium/', views.product_list, {'category_id': 2}, name='premium_list'),
    path('products/rolly-i-sushi/', views.product_list, {'category_id': 3}, name='rolly-i-sushi_list'),
    path('products/tempura/', views.product_list, {'category_id': 4}, name='tempura_list'),
    path('products/zapechyonnye/', views.product_list, {'category_id': 5}, name='zapechyonnye_list'),
    path('products/goryachee-i-salaty/', views.product_list, {'category_id': 6}, name='goryachee-i-salaty_list'),
    path('products/sousy/', views.product_list, {'category_id': 7}, name='sousy_list'),
    path('products/napitki-i-deserty/', views.product_list, {'category_id': 8}, name='napitki-i-deserty_list'),
    path('products/spetsii/', views.product_list, {'category_id': 9}, name='spetsii_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
