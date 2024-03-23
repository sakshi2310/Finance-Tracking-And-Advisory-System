"""
URL configuration for Personal_Finance_Tracking_and_Advisory_System project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from FinanceApp.views import *
# from FinanceApp.urls import *
from AdminFinanceApp.views import *
# from AdminFinanceApp.urls import *
from AdminFinanceApp.views import *
from django.views.generic import RedirectView


urlpatterns = [
 
    path('',home,name='home'),
    path('FinanceApp/',home,name='home'),
    path('FinanceApp/signup/',signup,name='signup'),
    path('FinanceApp/BasicInfo/',basic_info,name='BasicInfo'),
    path('FinanceApp/Login/',login,name='login'),
    path('FinanceApp/dashboard/',dashboard,name='dashboard'),
    path('FinanceApp/otp/',opt_verfication,name='opt_verfication'),
    path('FinanceApp/income/',income,name='income'),
    path('FinanceApp/logout/',logout,name='logout'),

    # Goals
    path('FinanceApp/add-Goals/',Add_Goals,name='Add_Goals'),
    path('FinanceApp/view-goals/',view_goals,name='view_Goal'),
    path('FinanceApp/single-goal/<int:single_goal_id>/',single_goal,name="single_goal"),

    # demo
    path('FinanceApp/demo/',demo,name='demo'),


    path('AdminFinanceApp/Admin-Login/',admin_Login,name='Login'),
    path('AdminFinanceApp/Admin-Register/',admin_Register,name='Register'),
    path('AdminFinanceApp/Admin-Dashboard/',admin_Dashboard,name='Dashboard'),
    path('AdminFinanceApp/Admin-Add-IncomeSource/',admin_Add_Income_Source,name='admin_Add_Income_Source'),
    path('AdminFinanceApp/Admin-View-IncomeSource/',admin_View_Income_Source,name='admin_Add_Amount_Type'),
    path('AdminFinanceApp/Admin-Add-ExpanceSource/',admin_Add_Expance_Source,name='admin_Add_Expance_Source'),
    path('AdminFinanceApp/Admin-View-ExpanceSource/',admin_View_Expance_Source,name='admin_Add_Amount_Type'),
    path('AdminFinanceApp/Admin-Add-AmountType/',admin_Add_Amount_Type,name='admin_Add_Amount_Type'),
    path('AdminFinanceApp/Admin-View-AmountType/',admin_View_Amount_Type,name='admin_Add_Amount_Type'),
    # path('AdminFinanceApp/Admin-View-AmountType/')
    path('admin/', admin.site.urls),
]
