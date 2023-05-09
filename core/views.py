import hashlib, requests, jwt
from datetime import datetime, timedelta

from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status

from sushidrop import settings
from .serializers import UserSerializer
from django.contrib.auth import login, get_user_model
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(password=hashlib.md5((serializer.validated_data['password']).encode()).hexdigest())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        User = get_user_model()
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user and check_password(hashlib.md5(password.encode()).hexdigest(), user.password):
            login(request, user)
            payload = {
                'user_id': user.id,
                'exp': datetime.utcnow() + timedelta(days=2)
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Ошибка авторизации'}, status=status.HTTP_401_UNAUTHORIZED)


def vk_oauth2_callback(request):
    code = request.GET.get('code')

    response = requests.post('https://oauth.vk.com/access_token', params={
        'client_id': settings.SOCIAL_AUTH_VK_OAUTH2_KEY,
        'client_secret': settings.SOCIAL_AUTH_VK_OAUTH2_SECRET,
        'redirect_uri': settings.SOCIAL_AUTH_VK_OAUTH2_REDIRECT_URI,
        'code': code
    })

    access_token = response.json().get('access_token')
    user_response = requests.get('https://api.vk.com/method/users.get', params={
        'access_token': access_token,
        'fields': 'email',
        'v': '5.130',
    })

    user_data = user_response.json().get('response')[0]
    request.session['user_data'] = user_data

    return redirect('http://localhost:8080/')

    # Вернуть данные о пользователе в формате JSON
    # print(user_response.json())
