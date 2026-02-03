from django.shortcuts import render

# Create your views here.


def layout_test(request):
    return render(request, "main_app/base.html")