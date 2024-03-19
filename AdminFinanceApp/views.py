from django.shortcuts import render
from AdminFinanceApp.models import *

# Create your views here.

def Login(request):
     return render(request,'Admin_Login.html')

def Register(request):
     AdminRegisterobj = Admin_RegisterForm()
     if 'Register' in request.POST:
          print("-------------------------------heloo------------------")
          AdminRegisterobj = Admin_RegisterForm(request.POST)
          AdminRegisterobj.save()
     return render(request,'Admin_Register.html',{'adminfrm':AdminRegisterobj})

def Dashboard(request):
     return render(request,'Admin_Dashboard.html')