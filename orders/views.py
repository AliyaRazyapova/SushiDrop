from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.auth import CustomJWTAuthentication
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
            serializer.save()
            return Response({'success': True, 'message': 'Order created successfully'})
        return Response({'success': False, 'message': serializer.errors})
