from django.db import models



class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.CharField(max_length=255)
    published_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titile

