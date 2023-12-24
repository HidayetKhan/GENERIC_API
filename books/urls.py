
from django.urls import path
from books.views import BooksListCreateView, BookDetailView

urlpatterns = [
    path('books/', BooksListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]