from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('categories/', views.list_categories, name='list_categories'),
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('nabory/', views.product_list, {'category_id': 1}, name='nabory_list'),
    path('premium/', views.product_list, {'category_id': 2}, name='premium_list'),
    path('rolly-i-sushi/', views.product_list, {'category_id': 3}, name='rolly-i-sushi_list'),
    path('tempura/', views.product_list, {'category_id': 4}, name='tempura_list'),
    path('zapechyonnye/', views.product_list, {'category_id': 5}, name='zapechyonnye_list'),
    path('goryachee-i-salaty/', views.product_list, {'category_id': 6}, name='goryachee-i-salaty_list'),
    path('sousy/', views.product_list, {'category_id': 7}, name='sousy_list'),
    path('napitki-i-deserty/', views.product_list, {'category_id': 8}, name='napitki-i-deserty_list'),
    path('spetsii/', views.product_list, {'category_id': 9}, name='spetsii_list'),
    path('<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
