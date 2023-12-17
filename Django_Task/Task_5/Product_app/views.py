from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

def Product_View(request):
    products=Product.objects.all()
    return render(request,'home.html',{'data':products})
# Create your views here.

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
          print('hello')
          form.save()
          return redirect('/product')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def Product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'Product_detail.html',{'data':product})
