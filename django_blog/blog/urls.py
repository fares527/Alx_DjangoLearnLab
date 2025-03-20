from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile, name='profile'),
    path('', views.PostListView.as_view, name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view, name='post_detail'),
    path('post/new/', views.PostCreateView.as_view, name='post_new'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view, name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view, name='post_delete'),
    path('post/<int:pk>/comments/new', views.post_detail.as_view, name=''post_detail),
    path('comment/<int:pk>/update/', views.CommentUpdataView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/create/', views.CommentCreateView.as_view(), name='comment_create'),




]