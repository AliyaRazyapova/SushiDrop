from rest_framework import serializers

from core.backends import User
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'order_time', 'total_price', 'delivery_time', 'delivery_method', 'payment_method']
