from django.shortcuts import render,redirect
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
# Create your views here.

#!homeView
def homeView(request):
    all_cars_latest = Car.objects.all().order_by('-created_date')[:3]
    featured_cars = Car.objects.all().order_by('-created_date').filter(is_featured=True)
    
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    
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
def contactView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        email_subject = "You have a new message from Carzone website regarding".format(subject)
        message_body = "Name : {} . Email : {} . Phone : {} . Message : {}".format(name,email,phone,message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
            email_subject,
            message_body,
            'riadalimammedovriad@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.add_message(request,messages.SUCCESS,'Thank you for contacting us.We will get back to you shortly')
        return redirect(request.path)
        
    return render(request,'pages/contact.html')
