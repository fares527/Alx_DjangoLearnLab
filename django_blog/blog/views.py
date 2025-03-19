from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

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


