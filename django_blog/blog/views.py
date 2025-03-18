from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

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