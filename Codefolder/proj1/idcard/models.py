from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name=models.CharField(max_length=64)
    std_class=models.CharField(max_length=10)
    section=models.CharField(max_length=10)
    roll_no=models.CharField(max_length=3)
    address=models.CharField(max_length=64)
    parents_name=models.CharField(max_length=64)
    contact=models.CharField(max_length=10)
    std_photo=models.ImageField(upload_to="uploads/")

    def __str__(self):
        return f" {self.name} {self.std_class} {self.parents_name}"

