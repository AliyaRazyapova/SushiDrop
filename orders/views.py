from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.auth import CustomJWTAuthentication
from .serializers import OrderSerializer


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'success': True, 'message': 'Order created successfully'})
        return Response({'success': False, 'message': serializer.errors})
