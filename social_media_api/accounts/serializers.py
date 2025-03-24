from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()