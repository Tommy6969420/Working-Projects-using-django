from django.shortcuts import render
from.models import Tasks
from.forms import TasksForm
# Create your views here.
def index(request):
    if request.method=="POST":
        form=TasksForm(request.POST)
        form.save()
        tasks=Tasks.objects.all()
        form=TasksForm()
        context={
            'form':form,
            "tasks":tasks,
        }
        return render(request,"tasksapp/index.html",context)
    form=TasksForm()
    tasks=Tasks.objects.all()
    context={
            'form':form,
            "tasks":tasks,
        }
    return render(request,"tasksapp/index.html",context)