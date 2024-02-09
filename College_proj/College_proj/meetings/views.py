from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Users
# Create your views here.
def authenticate(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        users=Users.objects.values("username","password")
        for i in range(users.count()):
            if username == users[i]["username"]:
                if password==users[i]["password"]:
                    data_to_pass = {"username":username}
                    request.session['data'] = data_to_pass
                    return redirect('/meetings/meeting/')
                context={'response':'Password Unmatched'}
                return render(request,"meetings/auth.html",context)
            context={'response':'Username not found'}
            return render(request,"meetings/auth.html",context)
    context={'response':'Please enter your credentials'}
    return render(request,"meetings/auth.html",context)
def  meetings(request):
    data_received = request.session.get('data', None)
    if data_received:
        context={
            'username':data_received['username']
        }
        return render(request,"meetings/meetings.html",context)
    else:
        return redirect('/meetings/auth/')
    
 