from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello():
    return HttpResponse("Salom")
def info():
    return HttpResponse("Info")