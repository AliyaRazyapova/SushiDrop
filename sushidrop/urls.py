from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/vk/callback/', views.vk_oauth2_callback, name='vk_oauth2_callback'),
]
