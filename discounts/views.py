from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from core.auth import CustomJWTAuthentication
from .models import Discount
from .serializers import DiscountSerializer


class DiscountView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)
