from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('secondpage/', views.second_page, name='second'),
    path('portafolio1/', views.portafolio1, name='portafolio1'),
    path('portafolio2/', views.portafolio2, name='portafolio2'),
    path('portafolio3/', views.portafolio3, name='portafolio3'),
    path('portafolio4/', views.portafolio4, name='portafolio4'),

]
