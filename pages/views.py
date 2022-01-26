from django.shortcuts import render
from cars.models import Car
from .models import *
# Create your views here.

#!homeView
def homeView(request):
    all_cars_latest = Car.objects.all().order_by('-created_date')[:3]#yeni sondan 3 dene car gedir Car modelinden databaseden
    featured_cars = Car.objects.all().order_by('-created_date').filter(is_featured=True)
    
    context = {
        'all_cars_latest': all_cars_latest,
        'featured_cars': featured_cars,
    }
    
    return render(request,'pages/home.html',context)

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
