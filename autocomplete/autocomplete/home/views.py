from django.shortcuts import render
from.models import Names
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,"home/index.html")

def search_autocomplete(request):
    search=request.GET.get("search")
    objs=Names.objects.filter(name__startswith=search)
    payload=[]
    if search:
        for obj in objs:
            payload.append(
                {
                    "obj":obj,
                }
            )
    return JsonResponse({
        "status":True,
        "payload":payload,
    })
