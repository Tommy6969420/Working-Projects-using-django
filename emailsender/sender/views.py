from django.conf import settings
from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,"sender/index.html")
def sender(request):
  if (request.GET):
        data=request.GET.dict()
        email_from=settings.EMAIL_HOST_USER
        mail=send_mail(data.get("subject"),data.get("message"),email_from,[data.get("email")],fail_silently=False,)
        params={
            "mail":mail,
            "email_from":email_from,
            "email_to":data.get("email"),
            "subject":data.get("subject"),
            "message":data.get("message"),

        }
        return render(request,"sender/index.html",params)
  else:
      return render(request,"sender/index.html")
