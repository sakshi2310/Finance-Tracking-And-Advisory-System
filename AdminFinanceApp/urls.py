from django.urls import path,include
from . import views

urlpatterns = [
   path('Admin-Login/',views.Login,name='Login'),
   path('Admin-Register/',views.Register,name='Register'),
   path('Admin-Dashboard/',views.Dashboard,name='Dashboard'),
]