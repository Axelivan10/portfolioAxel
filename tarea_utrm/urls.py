from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('secondpage', views.second_page, name='second'),
]
