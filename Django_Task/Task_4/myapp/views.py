from django.shortcuts import render,redirect
from .models import Post


def Home(request):
    posts=Post.objects.all()
    return render(request,'myapp/home.html',{'data':posts})

def Post_detail(request,id):
    print(id)
    post=Post.objects.get(id=id)
    return render(request,'myapp/Post_detail.html',{'data':post})

def Add_Post(request):
    if request.method == 'POST':
            title=request.POST['title']
            content=request.POST['postdesc']
            author=request.POST['author']
            post=Post(title=title,content=content,author=author)
            post.save()
            return redirect('/')        
    return render(request,'myapp/add_post.html')
    




# Create your views here.
