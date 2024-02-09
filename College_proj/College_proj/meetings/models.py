from django.db import models

# Create your models here.
from django.db import models
class Users(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=64,unique=True)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}"