from django.test import TestCase
from rest_framework.test import APIClient
from core.models import User
from products.models import Product, CategoryProduct
from .models import Order, OrderItem


class OrderViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@mail.com', password='test123')
        self.client.force_authenticate(user=self.user)
        self.category = CategoryProduct.objects.create(name='Category Name')
        self.product = Product.objects.create(name='Product Name', price=10.0, gramms=100, category=self.category)
        self.order_data = {
            'user': self.user.id,
            'total_price': 20.0,
            'delivery_time': '2023-05-27T10:00:00Z',
            'delivery_method': 'Courier',
            'payment_method': 'Credit Card',
            'order_items': [
                {
                    'product': self.product.id,
                    'quantity': 2,
                    'total_price': 20.0
                }
            ]
        }

    def test_create_order(self):
        response = self.client.post('/api/orders/', data=self.order_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['message'], 'Order created successfully')
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)

    def test_create_order_invalid_data(self):
        invalid_order_data = {
            'user': self.user.id,
            'total_price': 5.0,
            'delivery_time': '2023-05-27T10:00:00Z',
            'delivery_method': 'Courier',
            'payment_method': 'Credit Card',
            'order_items': [
                {
                    'product': self.product.id,
                    'quantity': -50,
                    'total_price': 5.0
                }
            ]
        }
        response = self.client.post('/api/orders/', data=invalid_order_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['success'], False)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(OrderItem.objects.count(), 0)

    def test_get_order_list(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
