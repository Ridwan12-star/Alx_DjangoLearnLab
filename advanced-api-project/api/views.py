from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ✅ List all books / Create new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Permissions: anyone can GET, only authenticated can POST
    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


# ✅ Retrieve / Update / Delete a single book
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: anyone can GET, only authenticated can PUT/PATCH/DELETE
    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
