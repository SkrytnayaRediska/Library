# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Author, Book, BookInstance, Genre
from django.views.generic import ListView, DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='Available').count()
    num_authors = Author.objects.all().count()

    return render(request, 'index.html',
                  {
                      'num_books': num_books,
                      'num_instances': num_instances,
                      'num_instances_available': num_instances_available,
                      'num_authors': num_authors
                  }
                  )


class BooksListView(ListView):
    model = Book
    context_object_name = 'my_book_list'
    template_name = 'books_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorsListView(ListView):
    model = Author
    context_object_name = 'authors_list'
    template_name = 'authors_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
