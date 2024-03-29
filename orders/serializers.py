from rest_framework import serializers

from products.models import Product
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'total_price']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'order_time', 'total_price', 'delivery_time', 'delivery_method',
                  'payment_method', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            product_id = order_item_data['product'].id
            quantity = order_item_data['quantity']
            total_price = order_item_data['total_price']
            product = Product.objects.get(id=product_id)

            order_item = OrderItem(
                order=order,
                product=product,
                quantity=quantity,
                total_price=total_price * quantity
            )
            order_item.save()

        return order
