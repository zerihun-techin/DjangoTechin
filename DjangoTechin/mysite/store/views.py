from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.

def store(request):
    yared  = shop.objects.all()
    
    output = ','.join([singleobject.price for singleobject in  yared])
    return HttpResponse(output)

    
    
    
