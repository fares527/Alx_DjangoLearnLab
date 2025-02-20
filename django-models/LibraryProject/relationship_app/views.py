from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth import login, logout, aauthenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Assuming you have a BookForm
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    text_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(text_list, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library' 


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = aauthenticate(username=username, password=password)
        if user is not None:
             login(request, user)
             return redirect('profile') # Redirect to user's profile or any other page
        else:
                form.add_error(None, "Invalid username or password")

    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
     logout(request)
     return redirect('login')

def register(request):
    if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid() :
               user = form.save()
               login(request, user)
               return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})            



@login_required
def profile(request):
    """Example protected view, requires login."""
    return render(request, 'profile.html', {'user': request.user})



def is_admin(user):
    if user.is_authenticated:
        try:
            return user.userprofile.role == 'Admin'
        except UserProfile.DoesNotExist:
            return False
    return False

def is_librarian(user):
    if user.is_authenticated:
        try:
            return user.userprofile.role == 'Librarian'
        except UserProfile.DoesNotExist:
            return False
    return False

def is_member(user):
    if user.is_authenticated:
        try:
            return user.userprofile.role == 'Member'
        except UserProfile.DoesNotExist:
             return False
    return False

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
