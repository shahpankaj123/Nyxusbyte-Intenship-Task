from django.shortcuts import render,redirect
from django.views import View
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm,UserLoginForm
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def send_mail_verify(email ,token):
           subject = 'Your account to be verified'
           message =token
           email_from = settings.EMAIL_HOST_USER
           recipient_list = [email,'aaryanshah615@gmail.com']
           send_mail(subject, message , email_from ,recipient_list)

class Signup(View): 
        form=UserSignupForm() 
        def get(self, request, *args, **kwargs):
            return render(request,'signup.html',{'form':self.form})  

        def post(self, request, *args, **kwargs):       
           form = UserSignupForm(request.POST)
           if form.is_valid():
             email = form.cleaned_data['email']
             password= form.cleaned_data['password']
             name=form.cleaned_data['name']
             if User.objects.filter(email=email):
               messages.warning(request,"Email Already Taken")
               return redirect('/')
             else:
                #send_mail_verify(email,123)
                my_user=User.objects.create_user(email=email,name=name)
                my_user.set_password(password)
                my_user.save()
                uid=urlsafe_base64_encode(force_bytes(my_user.id))
                token=PasswordResetTokenGenerator().make_token(my_user)
                link='http://127.0.0.1:8000/verify/'+uid+'/'+token
                print(link)
                #send_mail_verify(email,link)
                messages.success(request,"Please Verify your Account")
                return redirect('Login')
           else:
             return render(request,'signup.html',{'form':self.form}) 
           
     

class Login(View):
    form=UserLoginForm()
    def get(self, request, *args, **kwargs):
        return render(request,'login.html',{'form':self.form}) 
    def post(self, request, *args, **kwargs): 
        form = UserLoginForm(request.POST)
        if form.is_valid():
             email = form.cleaned_data['email']
             password= form.cleaned_data['password']
             user=User.objects.get(email=email)
             if user.tc:
              myuser = authenticate(email=email,password=password)
              if myuser is not None:
                login(request,myuser)
                messages.success(request,"Login successfully")
                return redirect('/blog/')
              else:
               messages.warning(request,"Password or Username donot match") 
             else:
                messages.success(request,"Please Verify your account")
                return redirect('Login')
                   
        else:
          return render(request,'login.html',{'form':self.form})

class Logout(View):
   def get(self, request, *args, **kwargs):
     logout(request)
     return redirect('Login')
   
class Verify(View):
    def get(self, request,uid,token, *args, **kwargs):
        id = smart_str(urlsafe_base64_decode(uid))
        user=User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user,token):
            messages.warning(request,"Token expired") 
            return redirect('Login')
        else:
            user.tc=True
            user.save()
            messages.success(request,"your email Verified")
            return redirect('Login')


            
       

