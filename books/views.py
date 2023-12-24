from django.shortcuts import render
from books.serializer import BooksSerializer
from books.models import Books
from rest_framework import generics
# Create your views here.

class BooksListCreateView(generics.ListCreateAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer
