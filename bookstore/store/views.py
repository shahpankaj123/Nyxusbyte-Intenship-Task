import pandas as pd
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.shortcuts import render, redirect
from .models.product import Product
from .models.customer import Customer

def entry(request):
    cart =request.session.get('cart')
    n=0
    if cart:
        n = 0
        for i,j in cart.items():
            n+=cart.get(i)
    return n
def about(request):
    n = entry(request)
   
    email = request.session.get('email')
    return render(request, 'about.html', {'email': email,'n':n})


def Login(request):
    n = entry(request)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = Customer.get_email(email)
        if user:
            flag = Customer.get_pass(password)
            if flag:
                messages.success(request, 'Login successfully !! ')
                request.session['email'] = email
                data = Customer.get_detail(email)
                if data:
                    request.session['first_name'] = data.first_name
                    request.session['last_name'] = data.last_name

                # request.session['name'] =
                return redirect('index')
            else:
                messages.error(request,'password invalid !!')
                return redirect('Login')
        else:
            messages.error(request, 'invalid email !')
            return redirect('Login')

    return render(request, 'login.html',{'n':n})


def cart(request):
    n = entry(request)
    totalPrice = 0
    email = request.session.get('email')
    rowdata = request.session.get('cart')
    if rowdata:
        pass
    else:
        return render(request, 'cart.html')
    data = {}
    for i, j in rowdata.items():
        product = Product.get_detail(i)
        if product:
            pass
        else:
            return render(request, 'cart.html')
        totalPrice = totalPrice + (j*product.pages)
        data[product]=j
    return render(request, 'cart.html', {'data': data,'n':n, 'email':email, 'totalPrice':totalPrice})

def signout(request):
    # request.session.get('cart'
    try:
        del request.session['email']
        del request.session['cart']
    except:
        pass
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')


def index(request):
    n = entry(request)
    email = request.session.get('email')
    product = Product.get_all_product()#[:540:10]

    if request.method == 'POST':
        proid = request.POST.get('proid')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(proid)
            print(quantity)
            if quantity:
                cart[proid] = quantity+1
            else:
                cart[proid]=1
        else:
            cart = {}
            cart[proid] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
    return render(request, 'index.html', {'products':product, 'email':email,'n':n})


def navbar(request):
    n = entry(request)
    email = request.session.get('email')
    if request.method=='POST':
        isbn = request.POST['search']
    final = Product.get_detail_isbn(isbn)

    if final:
        return render(request, 'detail.html', {'final':final,'n':n})
    return render(request, 'index.html', {'email':email,'n':n})


def contact(request):
    n = entry(request)
    email = request.session.get('email')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        textarea = request.POST.get('textarea')
        data = Contact(name=name, email=email, mobile=mobile, textarea=textarea)
        data.save()
        messages.success(request, 'your form submitted success fully')
    return render(request, 'contact.html', {'email': email,'n':n})


def checkout(request):
    email = request.session.get('email')
    n = entry(request)
    return render(request, 'checkout.html', {'n':n,'email':email})


def details(request):
    n = entry(request)
    email = request.session.get('email')

    return render(request, 'detail.html', {'email': email,'n':n})


def signup(request):
    n = entry(request)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        flag = Customer.get_email(email=email)

        if flag:
            messages.error(request, "username already exits please try some others")
            return redirect('signup')

        if phone.strip().isdigit()==False:
            messages.error(request, "phone no must be numeric!!")
            return redirect('signup')

        if len(password)<5:
            messages.error(request, "make a strong password!!")
            return redirect('signup')

        myuser = Customer(first_name=fname,last_name=lname,phone=phone, email=email, password=password)
        myuser.save()
        messages.success(request, "your account created successfully")

        request.session['email'] = email
        data = Customer.get_detail(email)
        if data:
            request.session['first_name'] = data.first_name
            request.session['last_name'] = data.last_name

        return render(request, 'index.html',{'email':email})

    return render(request, 'signup.html',{'n':n})


def account(request):
    n = entry(request)
    email = request.session.get('email')
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    return render(request, 'account.html', {'email':email, 'first_name':first_name,'last_name':last_name,'n':n})


