from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import users
from polls.models import FormModel, LoginUser, SingupUser
from django.contrib import messages
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


# def login(request):
#     return render(request, "login.html")
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = None

#         try:
#             user = LoginUser.objects.get(username=username, is_active=True)
#         except LoginUser.DoesNotExist:
#             messages.error(request, "Invalid username or password")
#         else:
#             if user.check_password(password):
#                 messages.success(request, f"Welcome, {username}!")
#                 return redirect("home_view")
#             messages.error(request, "Invalid username or password")

#     return render(request, "login.html")

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = None
#         # prefer singup users: fall back to legacy LoginUser if present
#         try:
#             user = SingupUser.objects.get(username = username, is_active=True)
#         except:

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = None

        try:
            user = SingupUser.objects.get(username=username, is_active=True)
        except SingupUser.DoesNotExist:
            try:
                user = LoginUser.objects.get(username=username, is_active=True)
            except LoginUser.DoesNotExist:
                user = None

        if user and user.check_password(password):
            messages.success(request, f"Welcome, {username}!")
            return redirect("home_view")
        
        messages.error(request, "Invalid username or password")

    return render(request, "login.html")

def singup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not email or not password:
            messages.error(request, "All fields are required")
        elif SingupUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif SingupUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            new_user = SingupUser(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            messages.success(request, "SingUp successful. you can now Log in.")
            return redirect("login_view")
        
    return render(request, "singup.html")

def arun(request):
    return render(request, "arun_index.html")

def layout(request):
    return render(request, "layout.html")