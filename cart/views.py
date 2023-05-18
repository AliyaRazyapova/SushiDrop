from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart_items(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data)
