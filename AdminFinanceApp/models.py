from django.db import models
from django.forms import ModelForm

# Create your models here.

class Admin_Register(models.Model):
     User_name = models.CharField(max_length=200)
     Email = models.CharField(max_length=200)
     Password = models.CharField(max_length=200)

class Admin_RegisterForm(ModelForm):
     class Meta:
          model = Admin_Register
          fields = '__all__'
