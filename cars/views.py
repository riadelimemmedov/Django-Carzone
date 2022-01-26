from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

#!allCarsView
def allCarsView(request):#request parametresi mutleq gelmelidir eger bu funksiyaa ye def her hansi bir url e baglidirsa cunki hemin url e request atilir istifadeci terefinden sonra bu funksyain tetikleyir
    context = {
        
    }
    
    return render(request,'cars/cars.html',context)

#!detailCars
def detailCarsView(request,id):
    
    single_car = get_object_or_404(Car,id=id)
    
    context = {
        'single_car':single_car
    }
    
    return render(request,'cars/cars_detail.html',context)