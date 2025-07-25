# relationship_app/query_samples.py

import os
import django

# Replace 'django_models' with the actual folder that contains settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "John Doe"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"\nBooks by {author.name}:")
    for book in books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'")

# List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")

# Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library '{library_name}'")
