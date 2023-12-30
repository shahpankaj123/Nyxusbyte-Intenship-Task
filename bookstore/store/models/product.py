from django.db import models


class Product(models.Model):
    author = models.CharField(max_length=100, default='')
    bookformat = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=1000, default='')
    genre = models.CharField(max_length=200, default='')
    img = models.ImageField(upload_to='product/')
    isbn = models.CharField(max_length=50, default='')
    link= models.CharField(max_length=200, default='')
    pages= models.IntegerField(default=0)
    rating= models.IntegerField(default=0)
    title = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return (str(self.id) + " "+self.title)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_detail(id=0):
        return Product.objects.get(id=id)

    @staticmethod
    def get_detail_isbn(isbn):
        return Product.objects.get(isbn=isbn)
