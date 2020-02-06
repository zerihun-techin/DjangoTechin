from django.shortcuts import render
from django.http import HttpResponse
from store.models import *

def books(request):
    hiwi = shop.objects.all()
    context ={
        'data':hiwi
    }
    
    return render(request,'books/index.html',context)

# Create your views here.
