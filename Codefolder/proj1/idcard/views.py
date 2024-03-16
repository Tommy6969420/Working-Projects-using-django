from django.shortcuts import render
from . models import StudentInfo
# Create your views here.

def index(request):
    stdsinfo=StudentInfo.objects.all()
    context={
        "stdsinfo":stdsinfo,
    }
    return render(request,"idcard/index.html",context)
  