from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)  

    def __str__(self) -> str:
        return self.name  


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

# Create your models here.
