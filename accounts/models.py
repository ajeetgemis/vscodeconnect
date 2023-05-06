from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
#from accounts import views
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=10,unique=True)
    otp=models.CharField(max_length=6)
    is_verified=models.BooleanField(default=False)


class authors(models.Model):
    author=models.CharField(max_length=20)

    def __str__(self):
        return self.author
    
class  books(models.Model):
    bookname=models.CharField(max_length=20)
    author=models.ForeignKey(authors,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return self.bookname  

 