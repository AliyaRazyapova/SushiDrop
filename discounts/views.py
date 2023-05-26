from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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

    @swagger_auto_schema(
        operation_description="Get discounts for a specific product",
        manual_parameters=[
            openapi.Parameter(
                name="product",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="Product ID"
            )
        ],
        responses={200: openapi.Response("OK", DiscountSerializer(many=True))}
    )
    def get(self, request):
        current_date = timezone.now().date()
        product_id = request.query_params.get('product')
        discounts = Discount.objects.filter(product_id=product_id, end_date__gte=current_date)
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)


class DiscountListView(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Get active discounts",
        responses={200: openapi.Response("OK", DiscountSerializer(many=True))}
    )
    def get(self, request):
        current_date = timezone.now().date()
        discounts = Discount.objects.filter(end_date__gte=current_date)
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)


class DiscountCreateView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a discount",
        request_body=DiscountSerializerCreate,
        responses={200: openapi.Response("OK"), 400: openapi.Response("Bad Request")}
    )
    def post(self, request):
        product_id = request.data['product']
        print(product_id)
        product = Product.objects.get(pk=product_id)
        print(product)
        serializer = DiscountSerializerCreate(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response({'success': True, 'message': 'Discount created successfully'})
        return Response({'success': False, 'message': serializer.errors})


class DiscountUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    @swagger_auto_schema(
        operation_description="Get a discount by ID",
        responses={200: openapi.Response("OK", DiscountSerializer())}
    )
    def get(self, request, discount_id):
        try:
            discount = Discount.objects.get(id=discount_id)
            serializer = DiscountSerializer(discount)
            return Response(serializer.data)
        except Discount.DoesNotExist:
            return Response({'message': 'Discount does not exist'}, status=404)
        except Exception as error:
            return Response({'message': str(error)}, status=500)

    @swagger_auto_schema(
        operation_description="Update a discount",
        request_body=DiscountSerializer,
        responses={200: openapi.Response("OK"), 400: openapi.Response("Bad Request")}
    )
    def put(self, request, discount_id):
        try:
            discount = Discount.objects.get(id=discount_id)
            serializer = DiscountSerializer(discount, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
        except Discount.DoesNotExist:
            return Response({'message': 'Discount does not exist'}, status=404)
        except Exception as error:
            return Response({'message': str(error)}, status=500)

    @swagger_auto_schema(
        operation_description="Delete a discount",
        responses={200: openapi.Response("OK"), 404: openapi.Response("Not Found"),
                   500: openapi.Response("Internal Server Error")}
    )
    def delete(self, request, discount_id):
        try:
            discount = Discount.objects.get(id=discount_id)
            discount.delete()
            return Response({'success': True, 'message': 'Discount deleted successfully'})
        except Discount.DoesNotExist:
            return Response({'success': False, 'message': 'Discount does not exist'})
        except Exception as e:
            return Response({'success': False, 'message': str(e)})
