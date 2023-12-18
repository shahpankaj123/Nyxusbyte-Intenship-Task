from django.urls import path
from .views import Product_View,Product_detail,add_product,edit_product,delete_product

urlpatterns = [
    path('',Product_View,name='Product_View'),
    path('product_detail/<int:id>',Product_detail,name='product_detail'),
    path('add_product/',add_product,name='add_product'),
    path('product_edit/<int:id>',edit_product,name='product_edit'),
    path('product_delete/<int:id>',delete_product,name='product_delete'),
]