from django.shortcuts import render,redirect
from .models import Blog,Category,Comment
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.views import View

@method_decorator(login_required(login_url='Login'), name='dispatch')
class Blog_View(View):
    def get(self, request):
     if cache.get('blogs'):
      blogs=cache.get('blogs')
      comment=Comment.objects.select_related()
      print('Redis Db')
     else:
        blogs=Blog.objects.select_related()
        comment=Comment.objects.select_related()
        cache.set('blogs',blogs,timeout=10)  
     return render(request,'home.html',{'data':blogs,'cmt':comment})
    
    def post(self,request):
       id=request.POST['id']
       cmt=request.POST['cmt']
       user=request.user
       comment=Comment.objects.create(cmt=cmt,user=user,blog=Blog.objects.get(id=id))
       if comment:
            messages.success(request,"Commented Successfully")
       return redirect('home')
       
          
       


@method_decorator(login_required(login_url='Login'), name='dispatch')
class add_blog(View):
    form = BlogForm()
    def get(self, request):
       return render(request, 'add_blog.html', {'form': self.form})

    def post(self, request):   
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            category= form.cleaned_data['category']
            desc=form.cleaned_data['desc']
            img=form.cleaned_data['img']
            user=request.user
            Blog.objects.create(name=name,user=user,category=category,desc=desc,img=img)
            messages.success(request,"Blog added successfully")
            return redirect('home')
        else:
          return render(request, 'add_blog.html', {'form': self.form})


@method_decorator(login_required(login_url='Login'), name='dispatch')
class Blog_detail(View):
   def get(self, request,id):
    blog=Blog.objects.get(id=id)
    return render(request,'Blog_detail.html',{'data':blog})

@method_decorator(login_required(login_url='Login'), name='dispatch')
class edit_blog(View):
  def get(self, request,id):
    self.blog=Blog.objects.get(id=id)
    if self.blog.user==request.user:
      category=Category.objects.all()
      return render(request, 'edit_blog.html', {'data':self.blog,'cat':category})
    else:
        messages.success(request,"You are not authorized to Edit blog")
        return redirect('home')
  def post(self, request,id):    
          name=request.POST['name']
          category1=request.POST['category']
          blog_desc=request.POST['desc']
          blog=Blog.objects.get(id=id)
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

@method_decorator(login_required(login_url='Login'), name='dispatch')
class delete_blog(View):
    def get(self, request,id):
      blog_obj=Blog.objects.get(id=id)
      if blog_obj.user==request.user:
        blog_obj.delete()
        messages.success(request,"Blog deleted successfully")
        return redirect('home')
      else:
        messages.success(request,"You are not authorized to Delete blog")
        return redirect('home')


