from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import users
from polls.models import FormModel
# Create your views here.

# def index(request):
#     return render(request, 'user_list.html')
def index(request):
    myusers = users.objects.all().values()
    templates = loader.get_template('user_list.html')
    context = {
        'myusers':myusers,
    }
    return HttpResponse(templates.render(context, request))

from .forms import InputForm

def home_view(request):
    context = {}
    context['form']=InputForm()
    return render(request, "home.html", context)

def form_view(request):
    if request.method == "POST":
        #print(request.POST) #
        title = request.POST.get("title")
        discription = request.POST.get("discription")

        u = FormModel(
            title=title,
            discription=discription,
            
        )
        u.save()

    return render(request, "form.html")


