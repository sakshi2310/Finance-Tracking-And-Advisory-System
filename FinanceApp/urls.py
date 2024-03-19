from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('Login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('otp/',views.opt_verfication,name='opt_verfication'),
    path('income/',views.income,name='income'),
    path('sidebar-header/',views.sidebar_header,name='sidebar_header'),
    path('logout/',views.logout,name='logout'),
    # GOOGLE URL
    path('accounts/',include('allauth.urls')),
]