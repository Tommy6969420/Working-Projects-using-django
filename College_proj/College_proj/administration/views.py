from django.shortcuts import render
from django.http import HttpResponse
from.forms import StudentForm
# Create your views here.
def index(request):
    return render(request,'administration/index.html')
def admission(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form=StudentForm()
            context={
                'form':form
            }
            return render(request,'administration/admission.html',context)
        return HttpResponse("invalid data")
    form=StudentForm()
    context={
               'form':form
            }
    return render(request,'administration/admission.html',context)