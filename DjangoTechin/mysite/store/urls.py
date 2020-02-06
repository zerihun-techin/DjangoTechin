from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.store, name='index1'),
   
]