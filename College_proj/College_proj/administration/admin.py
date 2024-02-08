from django.contrib import admin
from . models import Class, Student
# Register your models here.

admin.site.register(Class)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = ['course','gender',"admission_date"]
    search_fields = ['student_name','fathers_name','mothers_name','student_email',"course"]
    list_per_page= 10
