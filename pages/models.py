from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

#!Teams Model
class Teams(models.Model):
    first_name = models.CharField(max_length=255,verbose_name='First Name')
    last_name = models.CharField(max_length=255,verbose_name='Last Name')
    designation = models.CharField(max_length=255,verbose_name='Designation')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')#yeni year,month,date
    created_date = models.DateTimeField(auto_now_add=True)
    facebook_link = models.URLField(max_length=255,verbose_name='Facebook')
    twitter = models.URLField(max_length=255,verbose_name='Twitter')
    goggle_plus_link = models.URLField(max_length=255,verbose_name='GogglePlus')
    
    
    def __str__(self):
        return f"{self.first_name}--{self.last_name}"
    
    class Meta:
        verbose_name_plural = 'Teams'
    