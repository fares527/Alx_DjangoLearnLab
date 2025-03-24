from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()