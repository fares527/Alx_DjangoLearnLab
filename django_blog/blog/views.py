from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, PostForm, CommentForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

        else:
            form = CustomUserCreationForm()



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usernamae = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(usernamae=usernamae, password=password)

    else:
        form = AuthenticationForm()


def logout_view(request):
    logout(request)


def profile(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    else:
        form = CustomUserCreationForm()


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.hhtml'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/Post_detail.html'


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/Post_update.html'

    def test_func(self):
        Post = self.get_object()
        return self.request.user == Post.author


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'

    def test_func(self):
        Post= self.get_object()
        return self.request.user == Post.author


def post_detail(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save()
            Comment.post = post
            Comment.author = request.user
            Comment.save()
    
    else:
        form = CommentForm()




class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'blog/comment_form.html'
    form_class = CommentForm


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'