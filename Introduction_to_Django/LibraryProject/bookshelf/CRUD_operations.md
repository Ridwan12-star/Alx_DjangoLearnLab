# 📚 CRUD Operations in Django Shell


# 📘 Create Operation

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>
```



# 🔍 Retrieve Operation

```python
# Retrieve the book by title
book = Book.objects.get(title="1984")
book.title  # Output: '1984'
book.author  # Output: 'George Orwell'
book.publication_year  # Output: 1949

# Or display all attributes at once
print(book)
# Output: 1984 by George Orwell (1949)
```



# ✏️ Update Operation

```python
# Fetch the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
print(book)
# Output: Nineteen Eighty-Four by George Orwell (1949)
```



# ❌ Delete Operation

```python
# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
Book.objects.all()
# Output: <QuerySet []>
```