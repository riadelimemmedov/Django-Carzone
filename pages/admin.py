from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.

#!Custom Teams Model at the admin panel
class TeadAdmin(admin.ModelAdmin):
    
    #Upload Image
    def thumbnail(self,object):#object classdaki deyerleri ifade edir butun rowlari yeni
        return format_html('<img src="{}" width="50px" style="border-radius:50%;">'.format(object.photo.url))#Burdaki object yeni => object=Team modeline yeni classina
    thumbnail.short_description = 'Team Member Photo'
    ################################################################
    
    list_display = ['id','thumbnail','first_name','last_name','designation','created_date']
    list_display_links = ['id','thumbnail','first_name']
    search_filter = ['first_name','last_name','designation']
    list_filter = ['designation']
    
admin.site.register(Teams,TeadAdmin)