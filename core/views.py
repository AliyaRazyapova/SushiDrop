import jwt
import hashlib

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from sushidrop import settings
from core.models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from core.auth import CustomJWTAuthentication
from django.conf import settings


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

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


# def vk_oauth2_callback(request):
#     code = request.GET.get('code')
#
#     response = requests.post('https://oauth.vk.com/access_token', params={
#         'client_id': settings.SOCIAL_AUTH_VK_OAUTH2_KEY,
#         'client_secret': settings.SOCIAL_AUTH_VK_OAUTH2_SECRET,
#         'redirect_uri': settings.SOCIAL_AUTH_VK_OAUTH2_REDIRECT_URI,
#         'code': code
#     })
#
#     access_token = response.json().get('access_token')
#     user_response = requests.get('https://api.vk.com/method/users.get', params={
#         'access_token': access_token,
#         'fields': 'email',
#         'v': '5.130',
#     })
#
#     user_data = user_response.json().get('response')[0]
#     request.session['user_data'] = user_data
#
#     return redirect('http://localhost:8080/')


class UserProfileView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'email': user.email,
        }
        return Response(data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
