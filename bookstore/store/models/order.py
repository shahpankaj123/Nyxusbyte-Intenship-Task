from django.db import models

class Order(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=100)