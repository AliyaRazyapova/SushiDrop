import jwt
import hashlib
import requests
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseBadRequest, HttpResponse

from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_str, force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from sushidrop import settings
from core.models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from core.auth import CustomJWTAuthentication


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


import hashlib

@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = f"http://localhost:8080/reset-password-confirm/{uid}/{token}/"

    subject = 'Password Reset'
    context = {
        'user': user,
        'reset_link': reset_link,
    }
    html_message = render_to_string('password_reset_email.html',context)
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

    return Response({'success': 'Email sent'}, status=status.HTTP_200_OK)


def reset_password_confirm(request, uidb64, token):
    if request.method == 'GET':
        context = {
            'uidb64': uidb64,
            'token': token,
        }
        return render(request, 'index.html', context)

    if request.method == 'POST':
        uid = force_str(urlsafe_base64_decode(uidb64))
        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            return redirect('password_reset_invalid')

        if default_token_generator.check_token(user, token):
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')

            if new_password != confirm_new_password:
                return redirect('password_reset_invalid')

            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()

            user.password = hashed_password
            user.save()

            return redirect('password_reset_complete')

        return redirect('password_reset_invalid')