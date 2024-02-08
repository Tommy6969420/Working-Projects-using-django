from django.forms import ModelForm
from django import forms
from. models import Student
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets={
            "date_of_birth":forms.DateInput(attrs={'type': 'date', 
            'placeholder': 'yyyy-mm-dd (DOB)','class': 'form-control'
            }),
            'gender':forms.RadioSelect(),
            'course':forms.RadioSelect(),
            
        }
