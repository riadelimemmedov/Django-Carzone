from django.contrib import admin
from .models import *
# Register your models here.

#!ContactAdmin
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','car_first_name','car_last_name','car_email','car_city','create_date_message_notification']
    list_display_links = ['id','car_first_name','car_last_name']
    search_fields = ['car_first_name','car_last_name','car_email','car_title']
    list_per_page = 25#

admin.site.register(Contact,ContactAdmin)


