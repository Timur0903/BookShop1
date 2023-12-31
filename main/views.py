from django.shortcuts import render

from main.models import Book, Genre


# Create your views here.

def index(request):
    genres = Genre.objects.all()
    return render(request,'main/index.html',{'genres':genres})

def book_list(request,slug):
    books = Book.objects.filter(genre__slug=slug)
    return  render(request,'main/book_list.html',
                   {'books':books})