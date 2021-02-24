from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
	path('books/<int:book_id>', views.books, name='book_info'),
	path('add_author/<int:book_id>', views.add_author),
	path('authors', views.author_list),
	path('new_author', views.new_author),
	path('authors/<int:author_id>', views.author, name='author_info'),
	path('add_book/<int:author_id>', views.add_book),
]
