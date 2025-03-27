from django.urls import path
from .serializers import LoginSerializer, UserSerializer
from .views import UserCreate, UserProfile, LoginUser, follow_user, unfollow_user

urlpatterns = [
    path('register/',UserCreate.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user.as_view()),
    path('unfollow/<int:user_id>/', unfollow_user.as_view),
    #unfollow/<int:user_id>/", "follow/<int:user_id>"]
]