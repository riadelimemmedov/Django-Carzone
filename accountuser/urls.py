from os import name
from struct import pack
from django.urls import path
from . views import *

app_name = 'accountuser'

urlpatterns = [
    path('login',loginView,name='loginView'),
    path('register',registerView,name='registerView'),
    path('logout',logoutView,name='logoutView'),
    path('dashboard',dashboardView,name='dashboardView'),
]