from django.shortcuts import render, redirect
from FinanceApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
import random
from django.core.mail import EmailMessage


# Create your views here.
def home(request):
    return render(request, "index.html")


def signup(request):
    UserRegisterobj = User_RegisterForm()
    if "Register" in request.POST:
        UserRegisterobj = User_RegisterForm(request.POST)
        UserRegisterobj.save()
        return redirect("/Dashboard")

    # if 'Register_google' in
    return render(request, "Signup.html", {"userfrm": UserRegisterobj})


def login(request):
    if "user_id" in request.session:
        return redirect("/dashboard")
    if "login" in request.POST:
          Email = request.POST["Email"]
          Password = request.POST["Password"]
          obj = User_Register.objects.filter(Email=Email, Password=Password)
          
     
        # generate the random number
          otp = random.randint(1000, 9999)
          if obj.count() == 1:
               print(Email)
               row = obj.get()
               name = User_Register.objects.filter(Email=Email, Password=Password).get()
          
               print(name)
               # print(obj.Username)
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

               msg = EmailMessage(subject, message, email_form, email)
               msg.content_subtype = "html"  # Set the content type to HTML
               msg.send(fail_silently=False)

               # user session
               request.session["user_id"] = row.id

               # store the otp in the session
               request.session["otp"] = otp
               return redirect("/otp")
    return render(request, "Login.html")


def opt_verfication(request):
    # get the opt from the session
    otp = request.session.get("otp", None)
    print("server", otp)
    if "otp" in request.POST:
        user_otp = int(request.POST["otp"])
        print("user", user_otp)
        if user_otp == otp:

            # destory the session of otp
            if "otp" in request.session:
                del request.session["otp"]
            return redirect("/dashboard")

    return render(request, "otp.html")


def dashboard(request):
    return render(request, "dashboard.html")


def income(request):
    return render(request, "Add-income.html")


def sidebar_header(request):
    return render(request, "sidebar-header.html")


def logout(request):
    del request.session["user_id"]
    return redirect("/Login")
