from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.drink_list,name='list_of_drinks'),
    path('<int:drink_id>',views.drink_details,name='drink_details'),
]
