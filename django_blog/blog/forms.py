from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget, TagField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email' ,)

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(), required=False)
    class Meta:
        models = Post 
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    model = Comment
    fields = '__all__'