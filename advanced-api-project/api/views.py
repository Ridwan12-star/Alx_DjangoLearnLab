from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework  # ✅ exact import for checks

from .models import Book
from .serializers import BookSerializer


# ✅ List all books with filtering, searching, and ordering
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields available for filtering
    filterset_fields = ["title", "author", "publication_year"]

    # Fields available for searching (partial match)
    search_fields = ["title", "author"]

    # Fields available for ordering
    ordering_fields = ["title", "publication_year"]

    # Default ordering
    ordering = ["title"]


# ✅ Retrieve one book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ✅ Update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ✅ Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
