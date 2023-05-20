from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/', include('django.contrib.auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/vk/callback/', views.vk_oauth2_callback, name='vk_oauth2_callback'),
]
