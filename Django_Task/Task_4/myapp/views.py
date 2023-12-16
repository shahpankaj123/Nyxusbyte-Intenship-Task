from django.shortcuts import render,redirect
from .models import Post
from django.core.cache import cache


def Home(request): 
    if cache.get('posts'):
         posts=cache.get('posts')
         db='redis'
    else:     
      posts=Post.objects.all()
      db='sqlite'
      cache.set('posts',posts,timeout=10)
    print(db)     
    return render(request,'myapp/home.html',{'data':posts})

def Post_detail(request,id):
    if cache.get('post'):
        post=cache.get('post')
        db='redis'
    else:    
      post=Post.objects.get(id=id)
      db='sqlite'
      cache.set('post',post,timeout=10)
    print(db)  
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
