from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView

# Create your views here.
def Book_List(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, 'books/Book_List.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library' 