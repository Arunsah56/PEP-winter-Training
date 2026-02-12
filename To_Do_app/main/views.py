from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category


def home(request):
    categories = Category.objects.all()
    return render(request, "home.html", {"categories": categories})


def add_task(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        category_id = request.POST.get("category")

        category = Category.objects.get(id=category_id)
        Task.objects.create(title=title, category=category)

        return redirect("home")

    return render(request, "task_form.html", {"categories": categories})



def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    categories = Category.objects.all()

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.category_id = request.POST.get("category")
        task.completed = "completed" in request.POST
        task.save()

        return redirect("home")

    return render(request, "task_form.html", {
        "task": task,
        "categories": categories
    })



def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("home")

    return render(request, "confirm_delete.html", {"task": task})

def toggle_complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect("home")
