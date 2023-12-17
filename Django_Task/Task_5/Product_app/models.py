from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    desc=models.TextField()
    img=models.ImageField(upload_to='Product_img/')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

# Create your models here.
