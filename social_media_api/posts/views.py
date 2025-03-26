from django.shortcuts import render
from serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from models import Post, Comment, User


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    #queryset = Post.objects.all()
   # serializer_class = PostSerializer

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





        


