from django.shortcuts import render,redirect
from .models import Blog,Category
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='Login')
def Blog_View(request):
    blogs=Blog.objects.select_related()
    return render(request,'home.html',{'data':blogs})


@login_required(login_url='Login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          messages.success(request,"Blog added successfully")
          return redirect('home')
    else:
        form = BlogForm()

    return render(request, 'add_blog.html', {'form': form})


@login_required(login_url='Login')
def Blog_detail(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,'Blog_detail.html',{'data':blog})

@login_required(login_url='Login')
def edit_blog(request,id):
    blog=Blog.objects.get(id=id)
    category=Category.objects.all()
    if request.method == 'POST':
          name=request.POST['name']
          category1=request.POST['category']
          blog_desc=request.POST['desc']
          if request.FILES.get('img'):
               img=request.FILES.get('img')
               blog.img=img
          category_obj=Category.objects.get(name=category1)
          blog.name=name
          blog.category=category_obj
          blog.desc=blog_desc
          blog.save()
          messages.success(request,"Blog Updated successfully")
          return redirect('home')
    return render(request, 'edit_blog.html', {'data':blog,'cat':category})

@login_required(login_url='Login')
def delete_blog(request,id):
    blog_obj=Blog.objects.get(id=id)
    blog_obj.delete()
    messages.success(request,"Blog deleted successfully")
    return redirect('home')
