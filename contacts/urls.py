from django.urls import path
from .views import *

app_name = 'contacts'

urlpatterns = [
    path('inquiry',inquiryView,name='inquiryView'),
]