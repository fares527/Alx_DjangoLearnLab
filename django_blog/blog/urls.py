from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile, name='profile'),
    path('post/list', views.PostListView.as_view, name='post_list'),
    path('post/detail', views.PostDetailView.as_view, name='post_detail'),
    path('post/create', views.PostCreateView.as_view, name='post_create'),
    path('post/update', views.PostUpdateView.as_view, name='post_update'),
    path('post/delete', views.PostDeleteView.as_view, name='post_delete'),



]