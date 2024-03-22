from django.shortcuts import render, redirect
from FinanceApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
import random
from django.core.mail import EmailMessage
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):

    

    return render(request, "index.html")


def signup(request):
    UserRegisterobj = User_RegisterForm()
    duplicates = False
    if "save" in request.POST:
        email = request.POST['Email']
        users = User_Register.objects.filter(Email=email)
        if users.count() == 0:
            UserRegisterobj = User_RegisterForm(request.POST)
            UserRegisterobj.save()
            request.session['register_id'] = User_Register.objects.last().id
            return redirect("/FinanceApp/BasicInfo")
        else : 
            duplicates = True

    # if 'Register_google' in   
    return render(request, "Signup.html", {"duplicate":duplicates,"userfrm": UserRegisterobj})

def basic_info(request):
    if 'register_id' not in request.session:
        return redirect('/FinanceApp/signup')
    if 'save' in request.POST:
        reg_id = request.session['register_id']
        user = User_Register.objects.filter(id=reg_id).get()
        cash = request.POST['cash']
        card = request.POST['card']
        saving = request.POST['saving']
        obj = Personal_info(
            user_id = user,
            cash = cash,
            card = card,
            saving = saving
        )
        obj.save()
        income = request.POST['income']
        incometerm = request.POST['incometerm']
        expance = request.POST['expance']
        expanceterm = request.POST['incometerm']
        obj = average(
            user_id = user,
            income=income,
            incometerm=incometerm,
            expance=expance,
            expanceterm=expanceterm
        )
        obj.save()
        request.session['user_id'] = request.session['register_id']
        request.session['register_id'] = None
        return redirect ('/FinanceApp/dashboard')
    return render (request, "Basic_info.html")

def login(request):
    # if "user_id" in request.session:
    #     return redirect("/FinanceApp/dashboard")
    invalid_credentials = False
    if "login" in request.POST:
        Email = request.POST["Email"]
        Password = request.POST["Password"]
        obj = User_Register.objects.filter(Email=Email, Password=Password)
        otp = random.randint(1000, 9999)
        if obj.count() == 1:
            print(Email)
            row = obj.get()
            name = User_Register.objects.filter(Email=Email, Password=Password).get()
          
               # send the mail
            subject = "Welcome to Money Mentor Hub - Confirm Your Registration"
            message = f"""<html>
                              <head></head>
                              <body>
                              <p>Dear,{name.Username}</p>
                              <p>Thank you for choosing Money Mentor Hub for your finance tracking and advisory needs. We're excited to have you on board!</p>
                              <p>To complete your registration, please use the following one-time password (OTP):</p>
                              <p><strong>OTP: {otp}</strong></p>
                              <p>Please enter this OTP on the registration page to verify your email address and activate your account. If you didn't request this OTP, please disregard this email.</p>
                              <p>At Money Mentor Hub, we take the security of your information seriously. Rest assured that your data is protected with the highest level of encryption and security protocols.</p>
                              <p>If you have any questions or need further assistance, feel free to contact our support team at moneymentorhubb@gmail.com.</p>
                              <p>Welcome to Money Mentor Hub! We look forward to helping you achieve your financial goals.</p>
                              <p>Best regards,<br>Money Mentor Hub Team</p>
                              </body>
                              </html>"""
            email_form = settings.EMAIL_HOST_USER
            email = [
                    Email,
               ]
               # send_mail(subject, message, email_form, email, fail_silently=False)

            try:
                msg = EmailMessage(subject, message, email_form, email)
                msg.content_subtype = "html"  # Set the content type to HTML
                msg.send(fail_silently=False)
            except:
                print()

               # user session
            request.session["user_id"] = row.id

               # store the otp in the session
            request.session["otp"] = otp
            return redirect("/FinanceApp/otp/")
        else:
            invalid_credentials = True
        # generate the random number    
    return render(request, "Login.html",{'invalid_credentials': invalid_credentials})


def opt_verfication(request):
    # get the opt from the session
    otp = request.session.get("otp", None)
    if "otp" in request.POST:
        user_otp = int(request.POST["otp"])
        if user_otp == otp:
            # destory the session of otp
            if "otp" in request.session:
                del request.session["otp"]
            return redirect("/FinanceApp/dashboard")
    return render(request, "otp.html")


def dashboard(request):
    return render(request, "dashboard.html")

# def addincome(request):
#     userfrm = IncomeForm()
#     user = User_Register.objects.filter(id=request.session['user_id']).get()
#     sourses = Incomesource.objects.all()
#     types = Amounttype.objects.all()
#     if 'save' in request.POST:
#         userfrm = IncomeForm(request.POST)
#         userfrm.save()
#         return redirect ('/FinanceApp/income')
#     return render(request,'Add-income.html',{'sources':sourses,'types':types,'data':userfrm,'User_Id':user})
# def edit_income(request,edit_id):
#     user = User_Register.objects.filter(id=request.session['user_id']).get()
#     sourses = Incomesource.objects.all()
#     types = Amounttype.objects.all()
#     Frmobj = Income.objects.filter(id = edit_id).get()
#     obj = IncomeForm(instance=Frmobj)
#     if 'save' in request.POST:
#         obj = IncomeForm(request.POST,instance=Frmobj)
#         obj.save()
#         return redirect ('/FinanceApp/income') 
#     return render (request, 'Add-income.html',{'sources':sourses,'types':types,'data':obj,'User_Id':user})

# def delete_income(request,del_id):
#     Income.objects.filter(id=del_id).delete()
#     return redirect ('/FinanceApp/income')

def income(request):
    user = request.session['user_id']
    data = Income.objects.filter(user_id=user)
    return render(request, 'income.html',{'data':data})


def sidebar_header(request):
    return render(request, "sidebar-header.html")


def Add_Goals(request):
    user_id = User_Register.objects.filter(id= request.session['user_id']).get()
    print(user_id)
    Goalsobj = GoalsForm()
    if 'submit' in request.POST:
        # Goalsobj = GoalsForm(request.POST)
        name = request.POST['Goal_name']
        target_amount = request.POST['Target_amount']
        saved_amount = request.POST['Saved_amount']
        date = request.POST['Targe_date']

        obj = Goals(
            user_id = user_id,
            Goal_name = name,
            Target_amount = target_amount,
            Saved_amount = saved_amount,
            Targe_date  = date
        )
        obj.save()
        return redirect("/FinanceApp/view-goals")
        # Goalsobj.save()
    return render(request,'Add_Goals.html',{'goalfrm':Goalsobj,'Users_id':user_id})

def view_goals(request):
    per = 0
    all_goals = Goals.objects.all()
    record_count = Goals.objects.count()
    if record_count > 0:
        for row in all_goals:
            saved_amount = row.Saved_amount
            target_amount = row.Target_amount
            per =round(( saved_amount / target_amount )*100)
    return render(request,'View_Goals.html',{'all_goals':all_goals,'per':per})

cnt = 0
def single_goal(request,single_goal_id):
    global cnt
    goals = Goals.objects.filter(id=single_goal_id).get()
    if request.method == 'POST':
        if 'Edit_amount' in request.POST:
            cnt += 1
            saved = int(request.POST['Saved_amount'])
            goals.Saved_amount += saved
            goals.save()
            return HttpResponseRedirect(reverse('your_url_name'))
    return render(request,'Single-Goal.html',{'goals':goals})

def logout(request):
    del request.session["user_id"]
    return redirect("/FinanceApp/Login")

def demo(request):
    return render(request,'demo.html')
