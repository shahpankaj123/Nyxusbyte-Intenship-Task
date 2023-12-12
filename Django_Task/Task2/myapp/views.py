from django.shortcuts import render
from django.http import HttpResponse,JsonResponse



# Create your views here.
def Home(request):
    return HttpResponse("welcome to my page")

def About(request):
    return render(request,"about.html")

def Conatct(request):
    data={'id':1,'name':'pankaj','age':22}
    return JsonResponse(data)

def Productdetail(request):

    
    return render(request,'product.html',{'data':[
        {
            'id':1,
            'p_name':'shoes',
            'price':1200
        },
        {
            'id':2,
            'p_name':'book',
            'price':2200
        }
    ]})


