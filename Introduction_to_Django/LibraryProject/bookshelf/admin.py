from django.contrib import admin
from .models import Book

@admin.register(Book)  # A more concise way to register the model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the list view
    list_filter = ('author', 'publication_year')  # Filters in the right sidebar
    search_fields = ('title', 'author')  # Search bar for title and author
