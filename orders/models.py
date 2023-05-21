from django.db import models
from core.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.DateTimeField()
    delivery_method = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=255)
