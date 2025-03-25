from django.urls import path
from .serializers import LoginSerializer, UserSerializer
from .views import UserCreate, UserProfile, LoginUser

urlpatterns = [
    path('register/',UserCreate.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/', UserProfile.as_view(), name='profile')
]