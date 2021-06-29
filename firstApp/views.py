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
    