from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Discount
from .serializers import DiscountSerializer


class DiscountView(APIView):
    def get(self, request):
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)
