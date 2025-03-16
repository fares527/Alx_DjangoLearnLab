# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Author, Book
from .serializers import BookSerializer
from django.urls import reverse
from django.contrib.auth.models import User

class BookViewTests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book1 = Book.objects.create(title="Test Book 1", publication_year=2023, author=self.author)
        self.book2 = Book.objects.create(title="Test Book 2", publication_year=2024, author=self.author)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user) #Use force_login for testing session based auth.

    def test_book_list_view(self):
        #This test will pass because the user is logged in
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
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_book_create_view_unauthenticated(self):
        self.client.logout() #logout the user
        data = {'title': 'New Book', 'publication_year': 2025, 'author': self.author.pk}
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)
        self.client.force_login(user=self.user) #login again
        self.client.login()

    def test_book_update_view_authenticated(self):
        data = {'title': 'Updated Book', 'publication_year': 2026, 'author': self.author.pk}
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_book_update_view_unauthenticated(self):
        self.client.logout()
        data = {'title': 'Updated Book', 'publication_year': 2026, 'author': self.author.pk}
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_login(user=self.user)

    def test_book_delete_view_authenticated(self):
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_delete_view_unauthenticated(self):
        self.client.logout()
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2)
        self.client.force_login(user=self.user)

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