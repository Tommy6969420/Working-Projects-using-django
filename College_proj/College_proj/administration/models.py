from django.db import models
from django import forms 

# Create your models here.

class Class(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    GENDER_CHOICES=(('Male',"Male"),
        ('Female','Female'),
        ('Others','Others')
    )
    student_name=models.CharField(max_length=64)
    fathers_name=models.CharField(max_length=64)
    mothers_name=models.CharField(max_length=64)
    date_of_birth=models.DateField( auto_now=False, auto_now_add=False)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=10,default=False)
    present_address=models.CharField(max_length=64)
    permanent_address=models.CharField(max_length=64)
    student_phone_no=models.CharField(max_length=15)
    emergency_phone_no=models.CharField(max_length=15)
    course=models.ForeignKey(Class,on_delete=models.CASCADE)
    students_email=models.EmailField()
    accept_terms=models.BooleanField( )
    admission_date=models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.student_name} {self.course}'
class Instructor(models.Model):
    name=models.CharField(max_length=64)
    photo=models.ImageField(upload_to='instructors/')
    teacher_email=models.EmailField()
    qualification=models.CharField(max_length=64)
    experience=models.TextField()
    phone_no=models.CharField(max_length=15)
    address=models.CharField(max_length=64)
    # course=models.ForeignKey(Class,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'
class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery/')
    description=models.TextField()
    def __str__(self):
        return f'{self.description}'
class Notice(models.Model):
    name=models.CharField(max_length=64)
    description=models.TextField()