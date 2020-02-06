from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return HttpResponse("<h1> hello this is train app </h1>")
def news(request):
    
    return HttpResponse("<h1> hello this news app </h1>")
def event(request):
    
    return HttpResponse("<h1> hello this is event app </h1>")



   
