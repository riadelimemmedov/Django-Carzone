from django.shortcuts import render

# Create your views here.

#!allCarsView
def allCarsView(request):#request parametresi mutleq gelmelidir eger bu funksiyaa ye def her hansi bir url e baglidirsa cunki hemin url e request atilir istifadeci terefinden sonra bu funksyain tetikleyir
    context = {
        
    }
    
    return render(request,'cars/cars.html',context)