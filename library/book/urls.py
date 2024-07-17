from django.urls import path
from .views import IndexView,BooksView,DetalisBook

urlpatterns = [
  path('',IndexView.as_view(),name='index'),
  path('books/',BooksView.as_view(),name='books'),
  path('book_details/<int:pk>',DetalisBook.as_view(),name='book_details')
]