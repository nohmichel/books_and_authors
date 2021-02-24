from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse
# Create your views here.
def index(request):
	context = {
		"all_books":Book.objects.all(),
		"all_authors":Author.objects.all()
	}
	return render(request, "index.html", context)

def add_book(request):
	## adding a new book to list
	print('received request')
	new_book=Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
	return redirect('/')

def books(request, book_id):
	## lists book ID, DESC, and related authors
	context = {
		"one_book":Book.objects.get(id=book_id),
		"all_authors":Author.objects.all()
	}
	return render(request, "book_details.html", context)

def add_author(request, book_id):
	## GET LIST OF ALL AUTHORS
	author = Author.objects.get(id= request.POST['author_list'])
	## BOOK ID
	book = Book.objects.get(id=book_id)
	## ADDS AUTHOR TO BOOK
	book.authors.add(author)
	return redirect(f'/books/{book_id}')

def author_list(request):
	context = {
		"all_books":Book.objects.all(),
		"all_authors":Author.objects.all()
	}
	return render(request, "list_of_authors.html", context)

def new_author(request):
	## ADDS AUTHOR TO LIST
	print('received request')
	new_author=Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
	return redirect('/authors')

def author(request, author_id):
	## lists author ID, DESC, and related books
	context = {
		"one_author":Author.objects.get(id=author_id),
		"all_books":Book.objects.all()
	}
	return render(request, "author_details.html", context)

def add_book(request, author_id):
	## GET LIST OF ALL BOOKS
	book = Book.objects.get(id= request.POST['book_list'])
	## BOOK ID
	author = Author.objects.get(id=author_id)
	## ADDS AUTHOR TO BOOK
	author.books.add(book)
	return redirect(f'/authors/{author_id}')
