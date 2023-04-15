from django.db import models
from django.utils.translation import gettext_lazy as _
""" from django.contrib.auth.hashers import make_password """

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    user = models.CharField(max_length=50,null=False,unique=True,blank=False)
    email = models.EmailField(max_length=70,null=False,unique=True,blank=False)
    password = models.CharField(max_length=128,null=False,blank=False)
    
    