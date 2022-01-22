from django.shortcuts import render

# Create your views here.

#!homeView
def homeView(request):
    return render(request,'pages/home.html')

#!aboutView
def aboutView(request):
    return render(request,'pages/about.html')

#!servicesView
def servicesView(request):
    return render(request,'pages/services.html')

#!contactView
def contactView(request):#djangodaki view funksiyalari mutleq sekilde 1 ci parametr olarag request deyerini almalidir
    return render(request,'pages/contact.html')
