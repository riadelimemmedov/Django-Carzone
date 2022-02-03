from pyexpat import model
from django.db import models
from datetime import datetime

# Create your models here.

#!Contact Model
class Contact(models.Model):#models ele databasemizi temsil edir ve icindeki bagli oldugun databsenin funksiyalarinida hemcinin
    car_first_name = models.CharField(max_length=100)
    car_last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    car_customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    car_city = models.CharField(max_length=100)
    car_state = models.CharField(max_length=100)
    car_email = models.EmailField(max_length=100)
    car_phone = models.IntegerField()
    car_message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date_message_notification = models.DateTimeField(blank=True,default=datetime.now())#ve ya bu sekildede yazmag olardi => auto_now_add = True
    
    def __str__(self):
        return str(self.car_email)
    
#? eger => python manage.py makemigrations contacts yazsag gedib yalniz Contact modelini makemigrations edecek,Modelin adini kicik yazmlisan amma makemigrations sozunden sonra gelen adi yeni 
#? ve sonuna 's' elave etmelisen

