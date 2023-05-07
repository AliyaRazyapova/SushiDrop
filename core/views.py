import hashlib

from django.contrib.auth.hashers import make_password
from django.utils.crypto import constant_time_compare
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
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
            return Response({'message': 'Авторизация прошла успешно'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Ошибка авторизации'}, status=status.HTTP_401_UNAUTHORIZED)

