import hashlib
import jwt

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from sushidrop import settings
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = hashlib.sha256(validated_data['password'].encode()).hexdigest()
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=password)
        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'password']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        algorithm = 'HS256'
        secret_key = settings. SECRET_KEY
        token['algorithm'] = algorithm
        token = jwt.encode(token, secret_key, algorithm=algorithm)
        return token
