from django.db import models
class Users(models.Model):
    username=models.CharField(max_length=64,unique=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"