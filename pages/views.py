from django.shortcuts import render

# Create your views here.

#!homeView
def homeView(request):
    return render(request,'pages/home.html')