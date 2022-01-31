from django.shortcuts import render
from cars.models import Car
from .models import *
# Create your views here.

#!homeView
def homeView(request):
    all_cars_latest = Car.objects.all().order_by('-created_date')[:3]#yeni sondan 3 dene car gedir Car modelinden databaseden
    featured_cars = Car.objects.all().order_by('-created_date').filter(is_featured=True)
    
    model_search = Car.objects.all().values_list('model',flat=True).distinct() #eger flat=True yazmasam geriye tuple donderecek,yox eger flat=True yazsam geriye list donderecek
    city_search = Car.objects.all().values_list('city',flat=True).distinct()
    year_search = Car.objects.all().values_list('year',flat=True).distinct()
    body_style_search = Car.objects.all().values_list('body_style',flat=True).distinct()
    
    #search_fields = Car.objects.all().values('model','city','year','body_style').distinct() #Django icincde gelen VALUES acar sozu vasitesile secdiyimiz rowlari ala bilerik yalniz databasede yeni hansi rowlari isteyirik onlari ceke bilerik => values sayesinde
    # model_search = Car.objects.all().values_list('year').distinct()
    # model_search2 = Car.objects.all().values_list('model',flat=True).distinct()#flat=True olanda list seklinde gelir tuple deactive olur
    # print(model_search)
    # print('#############################')
    # print(model_search2)
    
    # for i in search_fields:
    #     print(i['model'])
    
    context = {
        'all_cars_latest': all_cars_latest,
        'featured_cars': featured_cars,
        
        ########################################################
        
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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
