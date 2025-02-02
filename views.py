from django.shortcuts import render
from django.http import HttpResponse

def say_something(request):
    return HttpResponse("Hello eli")
# Create your views here.
