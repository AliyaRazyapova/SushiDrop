import hashlib
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = hashlib.sha256(validated_data['password'].encode()).hexdigest()
        user = User.objects.create(email=validated_data['email'], password=password)
        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'password']
