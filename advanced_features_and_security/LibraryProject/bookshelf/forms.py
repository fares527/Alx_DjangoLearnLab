from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

    def clean_title(self):
        title = self.cleaned_data['title']
        # Example: Basic sanitization - remove leading/trailing spaces
        return title.strip()