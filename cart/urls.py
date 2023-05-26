from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView.as_view()),
    path('add/', views.CartAddView.as_view()),
    path('delete/', views.ClearCartView.as_view())
]
