from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("This is index page.")
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("This is contact page.")

def about(request):
    return HttpResponse("This is about page.")

def services(request):
    return HttpResponse("This is services page.")