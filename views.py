from django.shortcuts import render
from django.http import HttpResponse
def display(requset):
    s='<h1>"Hello Everyone"</h1>'
    return HttpResponse(s)

# Create your views here.
