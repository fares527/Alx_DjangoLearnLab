from relationship_app.models import Author, Book, Library, Librarian

# Sample data creation (for demonstration)
author1 = Author.objects.create(name="Jane Doe")
author2 = Author.objects.create(name="John Smith")

book1 = Book.objects.create(title="Python Basics", author=author1)
book2 = Book.objects.create(title="Django Advanced", author=author1)
book3 = Book.objects.create(title="Data Science 101", author=author2)

library1 = Library.objects.create(name="Main Library")
library1.books.add(book1, book2)

library2 = Library.objects.create(name="Branch Library")
library2.books.add(book3)

librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
librarian2 = Librarian.objects.create(name="Bob Williams", library=library2)

# Queries

# Query all books by a specific author
author_name = "Jane Doe"
author = Author.objects.get(name=author_name) #Get the author object.
books_by_author = Book.objects.filter(author=author) #Filter based on the author object.

print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = "Main Library"
books_in_main_library = Library.objects.get(name=library_name).books.all()
print(f"\nBooks in {library_name}:")
for book in books_in_main_library:
    print(book.title)

# Retrieve the librarian for a library
librarian_for_branch_library = Librarian.objects.get(library__name="Branch Library")
print("\nLibrarian for Branch Library:")
print(librarian_for_branch_library.name)

#Example of the needed Library query.
library_name_example = "Branch Library"
library_example = Library.objects.get(name=library_name_example)
print(f"\nExample Library: {library_example.name}")