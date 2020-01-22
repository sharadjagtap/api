from django.shortcuts import render

# Create your views here.
import datetime

from  django.http import HttpResponse
def about(request):
    return HttpResponse ("Hello this is parthudi...")


def contact(request):
    return  HttpResponse ("Hello conatct to my Sharad mamu")

def email(request):
    return HttpResponse("SharadJagtap19@gmail.com")

def time(request):
    time=datetime.datetime.now()
    s="Hello current date and time is:"+str(time)
    return HttpResponse(s)