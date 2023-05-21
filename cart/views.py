from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.auth import CustomJWTAuthentication
from .serializers import CartSerializer


class CartAddView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        print(data)
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Product added to cart successfully'})
        print(serializer.errors)
        return Response({'success': False, 'message': serializer.errors})

