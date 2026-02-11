from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return render(request, "home.html")

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Category


class HomeView(ListView):
    model = Category
    template_name = "home.html"
    context_object_name = "categories"


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'category']
    template_name = "task_form.html"
    success_url = reverse_lazy('home')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'category', 'completed']
    template_name = "task_form.html"
    success_url = reverse_lazy('home')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('home')
