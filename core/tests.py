import json
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from core.models import User


class RegisterViewTest(TestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {
            'email': 'test@test.ru',
            'first_name': 'test',
            'password': 'test'
        }

        json_data = json.dumps(data)
        response = self.client.post(url, json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@test.ru')
