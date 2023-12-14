from django.contrib import admin
from .models import Book,Author,Publisher,Genre


admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)

# Register your models here.
