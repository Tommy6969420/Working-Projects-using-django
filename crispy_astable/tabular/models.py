from django.db import models

# Create your models here.
class Bill(models.Model):
    'vendor','bill_date','due_date','reference'
    vendor=models.CharField(max_length=63)
    bill_date=models.DateField( auto_now=False, auto_now_add=False)
    due_date=models.DateField( auto_now=False, auto_now_add=False)
    reference=models.CharField(max_length=63)
