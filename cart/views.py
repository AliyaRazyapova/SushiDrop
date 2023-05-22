from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.auth import CustomJWTAuthentication
from .models import Cart
from .serializers import CartSerializer


class CartView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get cart items",
        responses={200: openapi.Response("OK", CartSerializer(many=True))}
    )
    def get(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)


class CartAddView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Product added to cart successfully'})
        return Response({'success': False, 'message': serializer.errors})

