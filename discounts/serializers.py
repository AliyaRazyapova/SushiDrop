from rest_framework import serializers

from products.serializers import ProductSerializer
from .models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Discount
        fields = '__all__'
