from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("This is index page.")
    return render(request, 'index.html')