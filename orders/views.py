from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.auth import CustomJWTAuthentication
from products.models import Product
from .models import OrderItem
from .serializers import OrderSerializer


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    @swagger_auto_schema(
        operation_description="Create an order",
        request_body=OrderSerializer,
        responses={200: openapi.Response("OK"), 400: openapi.Response("Bad Request")}
    )
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order_items = request.data.get('order_items', [])

            with transaction.atomic():
                order = serializer.save()

                order_items_data = []
                for item in order_items:
                    product_id = item.get('product')
                    quantity = item.get('quantity')
                    product = Product.objects.get(id=product_id)

                    order_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                        total_price=product.price * quantity
                    )
                    order_items_data.append(order_item)

            return Response({'success': True, 'message': 'Order created successfully'})

        return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)