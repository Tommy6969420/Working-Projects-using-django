from django.shortcuts import render
from django.http import HttpResponse
from checkuser.models import Users
def authenticate(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        users=Users.objects.values("username","password")
        for item in users:
            auth_user=item["username"]
            auth_password=item['password']
        print(auth_user)
        if username in auth_user:
            if password==auth_password:
               return HttpResponse("<h1>authenticated</h1>")
            return HttpResponse("<h1>Password Unmatched</h1>")
        return HttpResponse("<h1>Username unregistered</h1>")
    return render(request,"index.html")
        
            
    