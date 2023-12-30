from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    mobile = models.IntegerField()
    textarea = models.CharField(max_length=400)

    def __str__(self):
        return self.name