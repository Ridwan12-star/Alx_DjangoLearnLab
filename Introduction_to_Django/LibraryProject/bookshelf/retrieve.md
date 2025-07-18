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