from django.db import models
from django.forms import ModelForm

# Create your models here.

class Admin_Register(models.Model):
     User_name = models.CharField(max_length=200,default="")
     Email = models.CharField(max_length=200,unique=True,default="")
     Password = models.CharField(max_length=200,default="")

class Admin_RegisterForm(ModelForm):
     class Meta:
          model = Admin_Register
          fields = '__all__'

class Incomesource(models.Model):
     sourse = models.CharField(max_length=100)
     def __str__(self):
        return self.sourse

class IncomesourceForm(ModelForm):
     class Meta:
          model = Incomesource
          fields = "__all__"

class Expancesource(models.Model):
     sourse = models.CharField(max_length=100)
     def __str__(self):
        return self.sourse

class ExpancesourceForm(ModelForm):
     class Meta:
          model = Expancesource
          fields = "__all__"

class Amounttype(models.Model):
     type = models.CharField(max_length=100)
     def __str__(self):
        return self.type

class AmounttypeForm(ModelForm):
     class Meta:
          model = Amounttype
          fields = "__all__"