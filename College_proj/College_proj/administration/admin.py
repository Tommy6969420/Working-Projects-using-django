from django.contrib import admin
from . models import Class, Student, Instructor, Gallery, Notice
# Register your models here.

admin.site.register(Class)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = ['course','gender',"admission_date"]
    search_fields = ['student_name','fathers_name','mothers_name','student_email',"course"]
    list_per_page= 10
@admin.register(Instructor)
class InstructorsAdmin(admin.ModelAdmin):
    list_filter = ['qualification','experience']
    search_fields = ['name','teacher_email','qualification','experience']
    list_per_page= 10
admin.site.register(Gallery)
admin.site.register(Notice)


