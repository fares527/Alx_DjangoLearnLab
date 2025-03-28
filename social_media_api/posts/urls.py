from django.urls import path
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, FeedView



router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = router.urls


from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
     path('feed/', FeedView.as_view(), name='feed'),
]



urlpatterns = [
    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
]