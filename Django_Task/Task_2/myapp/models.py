from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=255)
    bio=models.TextField()

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book')
    title=models.CharField(max_length=100)
    published_date=models.DateField()

    def __str__(self) -> str:
        return self.title


# Create your models here.
