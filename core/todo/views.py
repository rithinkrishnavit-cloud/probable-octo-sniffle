from django.shortcuts import render, redirect
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

    return render(request, "todo/home.html")
