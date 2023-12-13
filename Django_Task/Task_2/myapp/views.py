from django.shortcuts import render
from .models import Book

# Create your views here.
def Home(request):
    book=Book.objects.all()
    return render(request,'myapp/home.html',{'data':book})
