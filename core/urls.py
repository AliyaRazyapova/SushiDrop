from django.urls import path
from core import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('auth/', views.UserRoleView.as_view(), name='check_authentication'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('reset-password-confirm/', views.reset_password_confirm)
]
