from django.urls import path
from .views import *

app_name = 'cars'

urlpatterns = [
    path('',allCarsView,name='allCarsView'),
    path('<int:id>',detailCarsView,name='detailCarsView'),
    path('search',searchView,name='searchView'),
    path('getdatacar',get_data_car,name='getdatacar'),
]