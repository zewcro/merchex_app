from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django </h1>')

def about(request):
    return HttpResponse('<h1>à propos</h1> <p> Nous adorons merch! </p>')