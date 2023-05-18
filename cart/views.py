from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart
from .serializers import CartSerializer
from django.contrib.auth.decorators import login_required


@login_required
@csrf_exempt
def get_cart_items(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    serializer = CartSerializer(cart_items, many=True)
    return JsonResponse(serializer.data, safe=False)


@login_required
@csrf_exempt
def add_to_cart(request):
    user = request.user
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))

    cart_item = Cart.objects.filter(user=user, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
        cart_item.save()
    else:
        cart_item = Cart.objects.create(user=user, product_id=product_id, quantity=quantity)

    serializer = CartSerializer(cart_item)
    return JsonResponse(serializer.data)
