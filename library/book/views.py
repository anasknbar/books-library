from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Book
# Create your views here.

class IndexView(TemplateView):
  template_name = "book/index.html"
  
class BooksView(ListView):
  model = Book
  template_name = 'book/books.html'
  context_object_name = 'books'
  
class DetalisBook(DetailView):
  model = Book
  template_name = 'book/book_details.html'
  context_object_name = 'book_details'
