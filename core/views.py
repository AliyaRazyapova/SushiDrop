import jwt
import hashlib
import requests

from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.cache import cache

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from sushidrop import settings
from core.models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from core.auth import CustomJWTAuthentication
from .tasks import send_password_reset_email


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="User registration",
        request_body=UserSerializer,
        responses={201: openapi.Response("Created"), 400: openapi.Response("Bad Request")}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="User login",
        request_body=UserSerializer,
        responses={200: openapi.Response("OK"), 401: openapi.Response("Unauthorized")}
    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            user = User.objects.get(email=email)
            if user.password == hashed_password:
                payload = {'email': email}
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').encode('utf-8')
                return Response({'token': token.decode('utf-8')}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def generate_jwt_token(user_data):
    payload = {
        'email': user_data['email']
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


def vk_oauth2_callback(request):
    code = request.GET.get('code')
    email = request.GET.get('state')

    response = requests.post('https://oauth.vk.com/access_token', params={
        'client_id': settings.SOCIAL_AUTH_VK_OAUTH2_KEY,
        'client_secret': settings.SOCIAL_AUTH_VK_OAUTH2_SECRET,
        'redirect_uri': settings.SOCIAL_AUTH_VK_OAUTH2_REDIRECT_URI,
        'code': code,
        'scope': 'email'
    })

    access_token = response.json().get('access_token')
    user_response = requests.get('https://api.vk.com/method/users.get', params={
        'access_token': access_token,
        'fields': 'first_name,last_name',
        'v': '5.130',
    })

    user_data = user_response.json().get('response')[0]
    user_data['email'] = email
    request.session['user_data'] = user_data

    first_name = user_data.get('first_name')
    last_name = user_data.get('last_name')
    phone_number = user_data.get('phone_number')
    address = user_data.get('address')

    try:
        user = User.objects.get(email=email)
        if user.first_name == first_name and user.last_name == last_name:
            jwt_token = generate_jwt_token(user_data)
            print(user_data)
            request.session['jwt_token'] = jwt_token

            redirect_url = f"http://localhost:8080/loginVK?jwt_token={jwt_token}"
            return redirect(redirect_url)
        else:
            return HttpResponse('Email already exists with different user data')
    except User.DoesNotExist:
        User.objects.create_user(email=email, password=None, first_name=first_name, last_name=last_name,
                                 phone_number=phone_number, address=address)

        jwt_token = generate_jwt_token(user_data)
        request.session['jwt_token'] = jwt_token

        redirect_url = f"http://localhost:8080/loginVK?jwt_token={jwt_token}"
        return redirect(redirect_url)


class UserProfileView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get user profile",
        responses={200: openapi.Response("OK")}
    )
    def get(self, request):
        user = request.user
        data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
            'address': user.address
        }
        return Response(data)

    @swagger_auto_schema(
        operation_description="Update user profile",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
                'address': openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        responses={200: openapi.Response("OK")}
    )
    def put(self, request):
        user = request.user
        data = request.data
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.phone_number = data.get('phone_number', user.phone_number)
        user.address = data.get('address', user.address)
        user.save()
        return Response({'message': 'Profile updated successfully'})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserRoleView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        user = request.user
        role = user.is_staff
        return Response({'role': role})


class ResetPasswordView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Reset password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        responses={200: openapi.Response("OK"), 400: openapi.Response("Bad Request")}
    )
    def post(self, request):
        email = request.data.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=400)

            token = default_token_generator.make_token(user)

            cache.set(token, user.id, timeout=60)

            reset_password_link = f'http://localhost:8080/reset-password/{token}/'
            send_password_reset_email(user, reset_password_link)

            return Response(status=200)
        else:
            return Response({'error': 'Email is required'}, status=400)


class NewPassword(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Set new password",
        manual_parameters=[
            openapi.Parameter(
                name="token",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        responses={200: openapi.Response("OK"), 400: openapi.Response("Bad Request")}
    )
    def post(self, request, token):
        user_id = cache.get(token)

        if not user_id:
            return Response({'error': 'Invalid or expired token'}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'Invalid or expired token'}, status=400)

        password = request.data.get('password')
        if password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            user.password = hashed_password
            user.save()

            cache.delete(token)

            return Response(status=200)
        else:
            return Response({'error': 'Password is required'}, status=400)
