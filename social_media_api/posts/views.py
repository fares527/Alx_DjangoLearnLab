from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions, status, generics
from .models import Post, Comment, CustomUser
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response




# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def Create(self):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

    def Retrieve(self):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

    def Update(self):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

    def Destroy(self):
        queryset = Post.objects.all()
        serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    def Create(self):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer

    def Retrieve(self):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer

    def Update(self):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer

    def Destroy(self):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer

@api_view('POST')
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if request.user != user_to_follow:
        request.user.following.add(user_to_follow)
        return Response({'message': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)
    return Response({'message': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view('POST')
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return  Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')

 



        


