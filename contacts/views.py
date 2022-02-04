from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import *

# Create your views here.

#!inquiryView
def inquiryView(request):
    if request.method == 'POST':
        #gelen deyerlerin hamsini dirnag icinde gotur yoxsa xeta verecek yeni POST requestden gelend deyerler
        user_id = request.POST.get('user_id')
        car_id = request.POST.get('car_id')#burdaki dirnag icindelo deyerler html terefinde inputun icide name attributunun  deyerleridir
        car_title = request.POST.get('car_title')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_need = request.POST.get('customer_need')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        contact = Contact(car_id=car_id,car_title = car_title,user_id = user_id,car_first_name = first_name,car_last_name = last_name,car_customer_need = customer_need,car_city = city,car_state = state,car_email = email,car_phone = phone,car_message = message)
        
        #eger birden cox her hansi masina contact yazmag isteyirnsense bunu engellemek ucun yazilan kod
        if request.user.is_authenticated:
            my_id = request.user.id
            find_contact = Contact.objects.all().filter(car_id=car_id,user_id=my_id)#bura => true ve ya false geri donecek
            if(find_contact):#bu cur yazilisda yeni True donubse,  eger false olmagini yoxlamag isteyirsenbse o zaman bu cur yazilcag => if(!find_contact) seklinde yazilmalidir
                messages.add_message(request,messages.ERROR,'You have already made an inquiry about this car. Please wait until we get back to you')
                return redirect(reverse('cars:detailCarsView',kwargs={'id':car_id}))#reverse sayesinde her hansi id li bir viewe dondere bilirem seyfeni proses bittikden sonra => return redirect(reverse('urlname',kwargs={'id':gelenid})) formasinda

        #*Send Email + contacta gelen bildirimler admin paneline dusenler ele bilki gmailimede dusecek istifadecilerin yazdigi datalar
        admin_info = User.objects.get(is_superuser=True)#get tek bir dene data getirir yeni 1 dene superuser olani getir odaki admindi onsuz => is_superuser yeniki bu admindir? sual verirem True beraberdirse beli admindir,yox eger false beraberdir admin deyil
        admin_email = admin_info.email
        
        send_mail(
            'New Car Inquiry',
            'You have a new inquiry this email: {} . Please login to your admin panel for more info'.format({email}),
            'riadalimammedovriad@gmail.com',#bura ile settings.py daki EMAIL_HOST_USER eyni olmalidir
            [admin_email],#yeni adminin mailine gelsin mesajlar
            fail_silently=False,#xetalari tutur => fail_silently
        )
        
        #eger Bir object yaradirsansa onu databaseye kayd elemek ucun => yaradilanobjectadi.save() edirsen
        contact.save()
        messages.add_message(request,messages.SUCCESS,'Your request has been submitted,we will get back to you shortly')
        return redirect(reverse('cars:detailCarsView',kwargs={'id':car_id}))