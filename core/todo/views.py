from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Todo
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]

        Todo.objects.create(user=request.user, title=title, description=description)
        return redirect("home")

    todo_items = Todo.objects.filter(user=request.user).order_by("complete", "id")

    return render(request, "todo/home.html", {"todo_items": todo_items})


@login_required
def delete_task(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == "POST":
        todo.delete()

    return redirect("home")


@login_required
def complete_task(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == "POST":
        todo.complete = True
        todo.save()

    return redirect("home")


@login_required
def update_task(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":
        todo.title = request.POST["title"]
        todo.description = request.POST["description"]
        todo.save()

        return redirect("home")

    todo_items = Todo.objects.filter(user=request.user).order_by("complete", "id")

    return render(
        request, "todo/home.html", {"todo_items": todo_items, "edit_task": todo}
    )
