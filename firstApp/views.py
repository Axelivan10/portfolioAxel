from django.http.response import HttpResponse
from django.shortcuts import render
import random


def home(request):
    return render( request,'ejercicio/home.html',{'nombre': 'Axel González'})

def second_page(request):
    num1 = int(request.GET.get('number1',0))
    num2 = int(request.GET.get('number2',0))
    resul = ''
    if request.GET.get('Suma'):
       resul = num1 + num2
    if request.GET.get('Resta'):
       resul = num1 - num2
    if request.GET.get('Multiplicacion'):
       resul = num1 * num2
    if request.GET.get('Division'):
       resul = num1 / num2


    return render(request,'ejercicio/second.html',{'second':resul})


def index(request):
    return render( request,'ejercicio/index.html')

def portafolio1(request):
    return render( request,'ejercicio/portfolio1.html')

def portafolio2(request):
    return render( request,'ejercicio/portfolio2.html')

def portafolio3(request):
    return render( request,'ejercicio/portfolio3.html')
   
def portafolio4(request):
    return render( request,'ejercicio/portfolio4.html')
   
   
   