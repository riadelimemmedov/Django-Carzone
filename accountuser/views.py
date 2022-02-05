from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from contacts.models import *


# Create your views here.

#!loginView
def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.add_message(request,messages.SUCCESS,'You Are Logged In')
            return redirect('accountuser:dashboardView')
        else:
            messages.add_message(request,messages.ERROR,'Invalid Login Credentials')
            return redirect(request.path)
    return render(request, 'accountuser/login.html')

#!registerView
def registerView(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if(User.objects.filter(username=username)).exists():
                messages.add_message(request,messages.INFO,'Username Already Exists')
                return redirect(request.path)
            else:
                if(User.objects.filter(email=email)).exists():
                    messages.add_message(request,messages.INFO,'Email Already Exists')
                    return redirect(request.path)
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)#create_user => avtomatik olarag useri.save edir databaseye => Creates, saves and returns a User.
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,'You are now logged in')
                    return redirect('accountuser:dashboardView')
        else:
            messages.add_message(request,messages.ERROR,'Password Do Not Match')
            return redirect(request.path)
    return render(request,'accountuser/register.html')

#!logoutView
def logoutView(request):
    if request.method == 'POST':
        logout(request)
        #messages.add_message(request,messages.SUCCESS,'You Are Successfully Logout')
        return redirect('pages:homeView')
    return redirect('pages:homeView')

#!dashboardView
@login_required(login_url='accountuser:loginView')
def dashboardView(request):
    user = request.user
    user_dashboardview = Contact.objects.filter(user_id=user.id).order_by('-create_date_message_notification')
    
    context = {
        'user_dashboardview':user_dashboardview,
    }
    
    return render(request,'accountuser/dashboard.html',context)