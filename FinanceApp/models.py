from django.db import models
from django.forms import ModelForm
from AdminFinanceApp.models import *

# Create your models here.

class User_Register(models.Model):
     Username = models.CharField(max_length=200,default='')
     Email = models.CharField(max_length=200,unique=True,default=True)
     Mobile_no = models.BigIntegerField(default=0)
     Password = models.CharField(max_length=200,default='')

class User_RegisterForm(ModelForm):
     class Meta:
          model = User_Register
          fields = '__all__'

class Personal_info(models.Model):
     user_id = models.ForeignKey(User_Register,on_delete=models.CASCADE)
     cash = models.BigIntegerField(default=0)
     card = models.BigIntegerField(default=0)
     saving = models.BigIntegerField(default=0)

class Personal_InfoForm(ModelForm):
     class Meta:
          model = Personal_info
          fields = '__all__'

class average(models.Model):
     user_id = models.ForeignKey(User_Register,on_delete=models.CASCADE)
     income = models.CharField(max_length=100,default="")
     incometerm = models.CharField(max_length=100,default="")
     expance = models.CharField(max_length=100,default="")
     expanceterm = models.CharField(max_length=100,default="")

class budgetForm(ModelForm):
     class Meta:
          model = average
          fields = '__all__'
     

class Expance(models.Model):
     user_id = models.ForeignKey(User_Register,on_delete=models.CASCADE)
     amount_type = models.CharField(max_length=100,default="")
     amount = models.CharField(max_length=100,default="")
     amount_sourse = models.ForeignKey(Incomesource,on_delete=models.CASCADE)
     date = models.DateTimeField()
     amount_status = models.CharField(max_length=100,default="")
     description = models.CharField(max_length=500,default="")

class ExpanceForm(ModelForm):
     class Meta:
          model = Expance
          fields = "__all__"

class Income(models.Model):
     user_id = models.ForeignKey(User_Register,on_delete=models.CASCADE)
     amount_type = models.ForeignKey(Amounttype,on_delete=models.CASCADE)
     amount = models.CharField(max_length=100,default="")
     amount_sourse = models.ForeignKey(Incomesource,on_delete=models.CASCADE)
     date = models.DateTimeField()
     amount_status = models.CharField(max_length=100,default="")
     description = models.CharField(max_length=500,default="")

class IncomeForm(ModelForm):
     class Meta:
          model = Income
          fields = "__all__"