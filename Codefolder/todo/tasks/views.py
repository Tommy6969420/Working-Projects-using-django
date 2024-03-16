from django.shortcuts import render
from. models import Tasks
# Create your views here.
def index(request):
    tasks=Tasks.objects.all()
    context={
        "tasks":tasks
    }
    return render(request,"tasks/index.html",context)