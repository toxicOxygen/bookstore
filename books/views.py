from django.views.generic import ListView,DetailView
from .models import Book

class ListBooksView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class DetailBookView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'