from django.shortcuts import render,redirect
from AdminFinanceApp.models import *

# Create your views here.

def admin_Login(request):
    if 'user_id' in request.session:
        return redirect ('/AdminFinanceApp/Admin-Dashboard')
    if 'save' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        obj = Admin_Register.objects.filter(Email=email,Password=password)
        if obj.count()==1:
            row = obj.get()
            request.session['user_id'] = row.id
            return redirect('/AdminFinanceApp/Admin-Dashboard')
    return render(request,'Admin_Login.html')

def admin_Register(request):
     AdminRegisterobj = Admin_RegisterForm()
     if 'Register' in request.POST:
          AdminRegisterobj = Admin_RegisterForm(request.POST)
          AdminRegisterobj.save()
          return redirect('/AdminFinanceApp/Admin-Dashboard')
     return render(request,'Admin_Register.html',{'adminfrm':AdminRegisterobj})

def admin_Dashboard(request):
     return render(request,'Admin_Dashboard.html')

def admin_Add_Income_Source(request):
    SourceObj = IncomesourceForm()
    if 'save' in request.POST:
        SourceObj = IncomesourceForm(request.POST)
        SourceObj.save()
        return redirect('/AdminFinanceApp/Admin-View-IncomeSource')
    return render(request,'Add_Income_Source.html',{'data':SourceObj})

def admin_View_Income_Source(request):
    data = Incomesource.objects.all()
    return render(request,'View_Income_Source.html',{'data':data})

def admin_Add_Expance_Source(request):
    SourceObj = ExpancesourceForm()
    if 'save' in request.POST:
        SourceObj = ExpancesourceForm(request.POST)
        SourceObj.save()
        return redirect('/AdminFinanceApp/Admin-View-ExpanceSource')
    return render(request,'Add_Expance_Source.html',{'data':SourceObj})

def admin_View_Expance_Source(request):
    data = Expancesource.objects.all()
    return render(request,'View_Expance_Source.html',{'data':data})

def admin_Add_Amount_Type(request):
    SourceObj = AmounttypeForm()
    if 'save' in request.POST:
        SourceObj = AmounttypeForm(request.POST)
        SourceObj.save()
        return redirect('/AdminFinanceApp/Admin-View-AmountType')
    return render(request,'Add_Amount_Type.html',{'data':SourceObj})

def admin_View_Amount_Type(request):
    data = Amounttype.objects.all()
    return render(request,'View_Amount_Type.html',{'data':data})