from django.urls import path
from .views import Product_View,Product_detail,add_product

urlpatterns = [
    path('',Product_View,name='Product_View'),
    path('product_detail/<int:id>',Product_detail,name='product_detail'),
    path('add_product/',add_product,name='add_product')
]