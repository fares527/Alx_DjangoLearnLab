from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

try:
    book = Book.objects.get(title="Nineteen Eighty-Four") #Try to retrieve it and see if it raises DoesNotExist
    print("Book still exists") #This will not run
except Book.DoesNotExist:
    print("Book deleted successfully")