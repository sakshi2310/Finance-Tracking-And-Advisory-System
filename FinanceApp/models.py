from django.db import models
from django.forms import ModelForm

# Create your models here.

class User_Register(models.Model):
     Username = models.CharField(max_length=200)
     Email = models.CharField(max_length=200)
     Mobile_no = models.BigIntegerField()
     Password = models.CharField(max_length=200)


class User_RegisterForm(ModelForm):
     class Meta:
          model = User_Register
          fields = '__all__'

