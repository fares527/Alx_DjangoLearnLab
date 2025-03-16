# api/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Author, Book
from .serializers import BookSerializer
from django.contrib.auth.models import User

class BookViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(name="Test Author")
        self.book1 = Book.objects.create(title="Test Book 1", publication_year=2023, author=self.author)
        self.book2 = Book.objects.create(title="Test Book 2", publication_year=2024, author=self.author)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.auth_headers = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token.key)}

    def test_book_list_view(self):
        response = self.client.get(reverse('book-list'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_detail_view(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_create_view_authenticated(self):
        data = {'title': 'New Book', 'publication_year': 2025, 'author': self.author.pk}
        response = self.client.post(reverse('book-create'), data, content_type='application/json', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_book_create_view_unauthenticated(self):
        data = {'title': 'New Book', 'publication_year': 2025, 'author': self.author.pk}
        response = self.client.post(reverse('book-create'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_update_view_authenticated(self):
        data = {'title': 'Updated Book', 'publication_year': 2026, 'author': self.author.pk}
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), data, content_type='application/json', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_book_update_view_unauthenticated(self):
        data = {'title': 'Updated Book', 'publication_year': 2026, 'author': self.author.pk}
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_book_delete_view_authenticated(self):
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book1.pk}), **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_delete_view_unauthenticated(self):
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_list_view_filter(self):
        response = self.client.get(reverse('book-list') + '?publication_year=2023')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_book_list_view_search(self):
        response = self.client.get(reverse('book-list') + '?search=Test%20Book%202')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 2')

    def test_book_list_view_ordering(self):
        response = self.client.get(reverse('book-list') + '?ordering=-publication_year')
        self.assertEqual(response.data[0]['title'], 'Test Book 2')
        self.assertEqual(response.data[1]['title'], 'Test Book 1')

