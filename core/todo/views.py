from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Todo


# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]

        add_task = Todo.objects.create(title=title, description=description)
        add_task.save()
        return redirect("home")

    todo_items = Todo.objects.order_by("complete", "id")

    return render(request, "todo/home.html", {"todo_items": todo_items})


def delete_task(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.delete()

    return redirect("home")


def complete_task(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.complete = True
        todo.save()

    return redirect("home")


def update_task(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == "POST":
        todo.title = request.POST["title"]
        todo.description = request.POST["description"]
        todo.save()

        return redirect("home")

    todo_items = Todo.objects.order_by("complete", "id")

    return render(
        request, "todo/home.html", {"todo_items": todo_items, "edit_task": todo}
    )
