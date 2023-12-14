
from django.urls import path
from .views import Home,Home2

urlpatterns = [
   path('',Home,name='home'),
   path('home/',Home2,name='home2')
]