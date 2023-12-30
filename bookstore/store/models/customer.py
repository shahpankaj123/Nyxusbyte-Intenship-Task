from django.db import models

class Customer(models.Model):
    # id = models.IntegerField(default=10)
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.first_name
    @staticmethod
    def get_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    @staticmethod
    def get_pass(password):
        try:
            return Customer.objects.get(password=password)
        except:
            return False

    @staticmethod
    def get_detail(email):
        return Customer.objects.get(email=email)