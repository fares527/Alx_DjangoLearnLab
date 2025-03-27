from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer

# Create your views here.
User = get_user_model
class UserCreate():
    queryset = User.object.all()
    serializer_class = UserSerializer



def LoginUser():
    serializer_class = LoginSerializer


class UserProfile():
    queryset = User.objects.all
    serializer_class = UserSerializer
    