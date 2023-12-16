from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('post_detail/<int:id>',views.Post_detail,name='post_detail'),
    path('add_post',views.Add_Post,name='add_post')
]