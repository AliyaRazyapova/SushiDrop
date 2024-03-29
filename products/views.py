from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db import transaction

from cart.models import Cart
from discounts.models import Discount
from orders.models import OrderItem
from products.models import CategoryProduct, Product


@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        gramms = request.POST.get('gramms')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        category = CategoryProduct.objects.get(id=category_id)
        product = Product(category=category, name=name, description=description, gramms=gramms, price=price, image=image)
        product.save()

        return JsonResponse({'success': True, 'message': 'Product created successfully!'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method!'})


def list_categories(request):
    categories = CategoryProduct.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def product_list(request, category_id=None):
    if category_id is None:
        products = Product.objects.all()
        data = [{'id': p.id, 'name': p.name, 'description': p.description, 'gramms': p.gramms, 'price': p.price, 'image': p.image.url, 'category': p.category.name} for p in products]
    else:
        category = get_object_or_404(CategoryProduct, id=category_id)
        products = Product.objects.filter(category=category)
        data = [{'id': p.id, 'name': p.name, 'description': p.description, 'gramms': p.gramms, 'price': p.price, 'image': p.image.url} for p in products]
    return JsonResponse(data, safe=False)


@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'gramms': product.gramms,
            'price': product.price,
            'image': product.image.url,
            'category': product.category.name
        }
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


@csrf_exempt
@transaction.atomic
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)

        Discount.objects.filter(product=product).delete()
        Cart.objects.filter(product=product).delete()
        OrderItem.objects.filter(product=product).delete()

        product.delete()

        return JsonResponse({'success': True, 'message': 'Product deleted successfully'})
    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Product does not exist'})
    except Exception as error:
        return JsonResponse({'success': False, 'message': str(error)})


@csrf_exempt
def edit_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)

        name = request.POST.get('name')
        description = request.POST.get('description')
        gramms = request.POST.get('gramms')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        product.name = name
        product.description = description
        product.gramms = gramms
        product.price = price

        if image:
            product.image = image

        product.save()

        return JsonResponse({'success': True, 'message': 'Product updated successfully'})
    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Product does not exist'})
    except Exception as error:
        return JsonResponse({'success': False, 'message': str(error)})
