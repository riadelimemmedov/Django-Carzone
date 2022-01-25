from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.

#!CarAdmin
class CarAdmin(admin.ModelAdmin):
    
    ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    def thumbnail(self,object):
        #format_html icerisinde sekili return etki fielslarda istifade ede bilek yeni => return format_html
        ################################################
        return format_html('<img src="{}" width="50px" style="border-radius:50%;">'.format(object.car_photo.url))#css de kodlar arasinda yeni parametler arasinda inline css yeni vergul qoyulmur yadda saxla qoyulmur
    thumbnail.short_description = 'Car Image'
    #################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    
    list_display = ['id','thumbnail','car_title','city','color','model','year','body_style','is_featured']
    list_display_links = ['id','thumbnail','car_title']
    list_editable = ['is_featured']
    search_fields = ['id','car_title','city','model','body_style','fuel_type']
    list_filter = ['city','model','body_style','fuel_type']

admin.site.register(Car,CarAdmin)   