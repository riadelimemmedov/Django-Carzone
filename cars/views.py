from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import *
# Create your views here.

#!allCarsView
def allCarsView(request):#request parametresi mutleq gelmelidir eger bu funksiyaa ye def her hansi bir url e baglidirsa cunki hemin url e request atilir istifadeci terefinden sonra bu funksyain tetikleyir
    cars = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars,4)
    page = request.GET.get('page')#reqem gelir burdadan butonlatdaki reqem yeni her tiklayanda get request atilir ele bil
    paged_cars = paginator.get_page(page)#yeni paginatora deyremki defaultdaki page deyernin ustune gel GET requestden gelen deyeri
    
    
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