import math

from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, 'index.html')


def sobrecarga(request: HttpRequest):
    sum = 0
    for i in range(10**7):
        sum += math.sqrt(i) * math.sin(i) * math.cbrt(i)
    return render(request, 'sobrecarga.html')
