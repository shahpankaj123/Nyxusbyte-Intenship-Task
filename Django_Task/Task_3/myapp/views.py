from django.shortcuts import render
from .models import Book,Publisher

# Create your views here

def Home(request):
    book = Book.objects.select_related('publisher').all()
    return render(request,'myapp/home.html',{'data':book})

def Home2(request):
    books = Book.objects.prefetch_related('authors', 'genres').all()
    return render(request, 'myapp/home2.html', {'data': books})

