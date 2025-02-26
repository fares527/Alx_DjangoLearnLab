# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from .forms import BookForm
from django.db.models import Q
from forms import ExampleForm




def book_list(request):
    query = request.GET.get('q')
    if query:
        # Using Django ORM to prevent SQL injection
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def form_example(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save() # Automatically handles validation
            return HttpResponse("Form submitted successfully")
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})


def books(request):
    """Alternative view for listing books (if needed)."""
    return book_list(request)  # Simply calls book_list

@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
    """Creates a new book."""
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        # ... other fields ...
        Book.objects.create(title=title, author=author)  # ... other fields ...
        return redirect('book_list')
    return render(request, 'bookshelf/book_create.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, book_id):
    """Edits an existing book."""
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        # ... update other fields ...
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_edit.html', {'book': book})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def book_delete(request, book_id):
    """Deletes a book."""
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('book_list')

def book_view(request, book_id):
    """Views a single book."""
    if request.user.has_perm('bookshelf.can_view_book'):
        book = get_object_or_404(Book, pk=book_id)
        return render(request, 'bookshelf/book_view.html', {'book': book})
    else:
        return HttpResponseForbidden("You do not have permission to view this book.")