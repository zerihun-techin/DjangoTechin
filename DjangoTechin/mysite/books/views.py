from django.shortcuts import render
from django.http import HttpResponse
from store.models import *
from . models import *

def books(request):
    hiwi = shop.objects.all()
    # context ={
    #     'data':hiwi
    # }
    
    return render(request,'index.html',{'data':hiwi})

# Create your views here.
