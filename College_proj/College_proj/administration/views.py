from django.shortcuts import render
from.forms import StudentForm
# Create your views here.
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