from django.db.models.signals import post_save, pre_delete
from users.models import User
from django.dispatch import receiver
from .models import Connect


@receiver(post_save, sender=User) 
def create_connect(sender, instance, created, **kwargs):
    if created:
        Connect.objects.create(user=instance)
  
@receiver(post_save, sender=User) 
def save_connect(sender, instance, **kwargs):
        instance.profile.save()