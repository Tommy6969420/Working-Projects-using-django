from django.shortcuts import render
from django.http import HttpResponse
from checkuser.models import Users
def authenticate(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        users=Users.objects.values("username","password")
        for i in range(users.count()):
            if username == users[i]["username"]:
                if password==users[i]["password"]:
                    return HttpResponse("<h1>authenticated</h1>")
                return HttpResponse("<h1>Password Unmatched</h1>")
        return HttpResponse("<h1>Username unregistered</h1>")
    return render(request,"index.html")
        
            
    