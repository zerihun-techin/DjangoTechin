from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>አለም ሰላም</h1>")

def getup(request):
    return HttpResponse("<H4> hello worl</H4>")