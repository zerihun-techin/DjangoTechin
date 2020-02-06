from django.shortcuts import render
from django.http import HttpResponse
from polls.models import *

def news(request):
    
    obj = login.objects.all()
   
    output = 'hello '.join([q.user for q in obj])
    return HttpResponse(output)

# latest_question_list = Question.objects.order_by('-pub_date')[:5]
# output = ', '.join([q.question_text for q in latest_question_list])
# return HttpResponse(output)




# Create your views here.
