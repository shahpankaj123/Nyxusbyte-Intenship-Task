from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import ProductForm
from django.contrib import messages

def Product_View(request):
    products=Product.objects.select_related()
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


def edit_product(request,id):
    product=Product.objects.get(id=id)
    category=Category.objects.all()
    if request.method == 'POST':
        if request.FILES.get('img'):
          name=request.POST['name']
          category1=request.POST['category']
          price=request.POST['price']
          product_desc=request.POST['desc']
          img=request.FILES.get('img')
          category_obj=Category.objects.get(name=category1)
          product.name=name
          product.category=category_obj
          product.price=price
          product.desc=product_desc
          product.img=img
          product.save()
          return redirect('/product')
        else:
          name=request.POST['name']
          category1=request.POST['category']
          price=request.POST['price']
          product_desc=request.POST['desc']
          category_obj=Category.objects.get(name=category1)
          img=product.img
          product.name=name
          product.category=category_obj
          product.price=price
          product.desc=product_desc
          product.img=img
          product.save()
          return redirect('/product')

    return render(request, 'edit_product.html', {'data':product,'cat':category})

def delete_product(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    messages.success(request,"Data deleted successfully")
    return redirect('home')

