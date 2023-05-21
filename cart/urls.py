from django.urls import path
from cart import views

urlpatterns = [
    path('add/', views.CartAddView.as_view())
]
