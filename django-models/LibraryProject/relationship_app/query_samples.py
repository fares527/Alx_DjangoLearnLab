from relationship_app.models import Author, Book, Library, Librarian

# Sample data creation (for demonstration)
author1 = Author.objects.create(name="Jane Doe")
author2 = Author.objects.create(name="John Smith")

book1 = Book.objects.create(title="Python Basics", author=author1)
book2 = Book.objects.create(title="Django Advanced", author=author1)
book3 = Book.objects.create(title="Data Science 101", author=author2)

library1 = Library.objects.create(name="library_name")
library1.books.add(book1, book2)

library2 = Library.objects.create(name="Branch Library")
library2.books.add(book3)

librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
librarian2 = Librarian.objects.create(name="Bob Williams", library=library2)


# Queries

# Query all books by a specific author
books_by_jane = Book.objects.filter(author__name="Jane Doe")
print("Books by Jane Doe:")
for book in books_by_jane:
    print(book.title)

# List all books in a library
library_name = "Main Library"  # Use a variable here
books_in_main_library = Library.objects.get(name=library_name).books.all()
print(f"\nBooks in {library_name}:") #use f-strings for clarity
for book in books_in_main_library:
    print(book.title)

# Retrieve the librarian for a library
librarian_for_branch_library = Librarian.objects.get(library__name="Branch Library")
print("\nLibrarian for Branch Library:")
print(librarian_for_branch_library.name)

#Example of the needed query, even if not used in previous examples.
library_name_example = "Branch Library"
library_example = Library.objects.get(name=library_name_example)
print(f"\nExample Library: {library_example.name}")