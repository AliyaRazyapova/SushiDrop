from django.db import models
from core.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.DateTimeField()
    delivery_method = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=255)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
