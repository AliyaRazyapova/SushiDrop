from django.test import TestCase
from core.models import User
from rest_framework.test import APIClient
import json
from datetime import date
from django.utils import timezone
from django.urls import reverse
from products.models import CategoryProduct, Product
from .models import Discount


class DiscountTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@mail.ru', password='test123')
        self.client.force_authenticate(user=self.user)

        self.category = CategoryProduct.objects.create(name='Category')
        self.product = Product.objects.create(
            category=self.category,
            name='Product Name',
            description='Product Description',
            gramms=100,
            price=100.0,
            image='img/product.jpg'
        )
        self.discount = Discount.objects.create(
            product=self.product,
            discount_percentage=3.0,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timezone.timedelta(days=7)
        )

    def test_get_discounts_for_product(self):
        url = reverse('discounts')
        data = {'product': self.product.id}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['product']['id'], self.product.id)

    def test_get_all_discounts(self):
        url = reverse('discounts_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['product']['id'], self.product.id)

    def test_create_discount(self):
        url = reverse('create_discounts')
        data = {
            'product': self.product.id,
            'discount_percentage': 5.0,
            'start_date': str(date.today()),
            'end_date': str(date.today() + timezone.timedelta(days=30))
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(Discount.objects.count(), 2)
