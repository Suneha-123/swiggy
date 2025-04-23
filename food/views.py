from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def biryani(request):
    return HttpResponse("i like biryani")

def icecream(request):
    return HttpResponse("i really love to eat ice creams")