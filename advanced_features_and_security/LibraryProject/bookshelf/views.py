# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponseForbidden

def book_list(request):
    """Lists all books."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

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