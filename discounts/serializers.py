from rest_framework import serializers

from products.models import Product
from products.serializers import ProductSerializer
from .models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Discount
        fields = '__all__'


class DiscountSerializerCreate(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Discount
        fields = ['product', 'discount_percentage', 'start_date', 'end_date']
