from django.shortcuts import render
from django.template import context
from .models import *
# Create your views here.

#!homeView
def homeView(request):
    return render(request,'pages/home.html')

#!aboutView
def aboutView(request):
    teams = Teams.objects.all()

    context = {
        'teams':teams,
    }

    return render(request,'pages/about.html',context)

#!servicesView
def servicesView(request):
    return render(request,'pages/services.html')

#!contactView
def contactView(request):#djangodaki view funksiyalari mutleq sekilde 1 ci parametr olarag request deyerini almalidir
    return render(request,'pages/contact.html')
