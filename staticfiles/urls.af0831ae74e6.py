from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('',homeView,name='homeView'),
    path('about',aboutView,name='aboutView'),
    path('services',servicesView,name='servicesView'),
    path('contact',contactView,name='contactView'),
]