from django.urls import path
from core import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('auth/', views.UserRoleView.as_view(), name='check_authentication'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('reset-password/<str:token>/', views.NewPassword.as_view(), name='new_password'),
]
