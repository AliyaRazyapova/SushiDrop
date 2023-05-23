from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Discount
from .serializers import DiscountSerializer
from django.utils import timezone


class DiscountView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        current_date = timezone.now().date()
        discounts = Discount.objects.filter(end_date__gte=current_date)
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)
