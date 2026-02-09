from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {"name":"Arun Sah"})

def jinja_page(request):
    return render(request, "dashboard.jinja", {"name":"Arun"})