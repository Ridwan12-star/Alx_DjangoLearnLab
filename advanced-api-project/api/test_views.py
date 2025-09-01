from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from .models import Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Authenticated client
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass123")

        # Create sample books
        self.book1 = Book.objects.create(title="Django for Beginners", author="William", publication_year=2020)
        self.book2 = Book.objects.create(title="Python Tricks", author="Dan", publication_year=2018)

        # API endpoints
        self.list_url = reverse("book-list")    # maps to BookListView
        self.detail_url = reverse("book-detail", args=[self.book1.id])
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book2.id])

    # ---------- CRUD TESTS ----------
    def test_list_books(self):
        """Ensure we can list all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Ensure authenticated users can create a book"""
        data = {"title": "New Book", "author": "AuthorX", "publication_year": 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create a book"""
        client = APIClient()  # unauthenticated
        data = {"title": "Unauthorized Book", "author": "NoAuth", "publication_year": 2021}
        response = client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_book(self):
        """Ensure we can retrieve a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_update_book(self):
        """Ensure authenticated users can update a book"""
        data = {"title": "Updated Django Book", "author": "William", "publication_year": 2021}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_delete_book(self):
        """Ensure authenticated users can delete a book"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTERING, SEARCHING, ORDERING ----------
    def test_filter_books_by_author(self):
        """Ensure filtering works"""
        response = self.client.get(self.list_url, {"author": "William"})
        s
