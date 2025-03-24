from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from rest_framework.authtoken.models import Token

User = get_user_model().objects.create_user

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:

                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled')
                Token = Token.objects.create(user=user)
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')
