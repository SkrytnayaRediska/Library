from django.urls import path, re_path
from .views import index, BooksListView, BookDetailView, AuthorsListView, AuthorDetailView

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^books/$', BooksListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', AuthorsListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', AuthorDetailView.as_view(), name='author-detail'),
]