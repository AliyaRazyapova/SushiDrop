from core.models import User
from django.test import TestCase
from rest_framework.test import APIClient


class CartViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@example.com', password='test123')
        self.client.force_authenticate(user=self.user)

    def test_get_cart_items(self):
        response = self.client.get('/api/cart/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
