from django.shortcuts import render,get_object_or_404,HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
import json
from django.core import serializers
from django.http import JsonResponse
from .models import *
# Create your views here.

#!allCarsView
def allCarsView(request):
    cars = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    context = {
        'cars': paged_cars,
    }
    
    return render(request,'cars/cars.html',context)

#!detailCars
def detailCarsView(request,id):
    
    single_car = get_object_or_404(Car,id=id)
    
    context = {
        'single_car':single_car
    }
    
    return render(request,'cars/cars_detail.html',context)

#!searchView
def searchView(request):
    cars = Car.objects.all().order_by('-created_date')
    
    ##########################################################################################################
    carname = request.GET.get('carname')
    select_model = request.GET.get('select-model')
    
    print(select_model)
    
    if carname:
        find_cars = Car.objects.filter(Q(car_title__icontains=carname)|
                                       Q(model__icontains=carname)|
                                       Q(description__icontains = carname)|
                                       Q(state__icontains=carname)|
                                       Q(city__icontains=carname))
    
    else:
        find_cars = Car.objects.all().order_by('-created_date')
        
    context = {
        'cars':cars,
        'find_cars':find_cars
    }
    return render(request,'cars/search.html',context)


#!Car Search With Ajax
def get_data_car(request):
    if request.is_ajax():
            if request.method == 'POST':
                carname = request.POST.get('CarName')
                model = request.POST.get('Model')
                location = request.POST.get('Location')
                year = request.POST.get('Year')
                bodystyle = request.POST.get('BodyStyle')
                carprice_max= request.POST.get('CarPriceMax')
                carprice_min = request.POST.get('CarPriceMin')
                
                result_price_car = 0
                
                if(carprice_max=='' and carprice_min==''):
                    result_price_car = 150000
                else:
                    result_price_car = (int(carprice_max) - int(carprice_min))            
                
                if(carname=='' or model == '' or year=='' or location =='' or bodystyle==''):
                    netice = Car.objects.all()
                    
                else:
                    netice = Car.objects.filter(#Q(car_title=carname)|
                                                Q(model=model)|
                                                Q(city=location)|
                                                Q(year=year)|
                                                Q(body_style=bodystyle)|
                                                Q(price=result_price_car)).distinct()
                data = serializers.serialize('json',netice)
                return JsonResponse({"cars_list":data})



    
    
    