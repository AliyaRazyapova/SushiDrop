from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from core.auth import CustomJWTAuthentication
from products.models import Product
from .models import Discount
from .serializers import DiscountSerializer, DiscountSerializerCreate
from django.utils import timezone


class DiscountView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        current_date = timezone.now().date()
        product_id = request.query_params.get('product')
        discounts = Discount.objects.filter(product_id=product_id, end_date__gte=current_date)
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)


class DiscountListView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        current_date = timezone.now().date()
        discounts = Discount.objects.filter(end_date__gte=current_date)
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)


class DiscountCreateView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data['product']
        print(product_id)
        product = Product.objects.get(pk=product_id)
        print(product)
        serializer = DiscountSerializerCreate(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(product=product)  # Pass the product object
            return Response({'success': True, 'message': 'Discount created successfully'})
        return Response({'success': False, 'message': serializer.errors})
