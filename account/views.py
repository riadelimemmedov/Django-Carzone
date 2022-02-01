from django.shortcuts import render,redirect

# Create your views here.

#!loginView
def loginView(request):
    return render(request, 'account/login.html')

#!registerView
def registerView(request):
    if request.method == 'POST':
        print('request method atildi')
    return render(request,'account/register.html')

#!logoutView
def logoutView(request):
    return redirect('pages:homeView')#mutleq sekilde return ile yazmalisan redirect funksiyasini

#!dashboardView
def dashboardView(request):
    return render(request,'account/dashboard.html')