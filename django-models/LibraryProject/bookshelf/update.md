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