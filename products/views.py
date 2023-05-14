from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
    return JsonResponse(data, safe=False)


@csrf_exempt
def product_list(request):
    products = Product.objects.all()
    data = [{'id': p.id, 'name': p.name, 'description': p.description, 'gramms': p.gramms,'price': p.price, 'image': p.image.url, 'category': p.category.name} for p in products]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


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
