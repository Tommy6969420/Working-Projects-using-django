from django.db.models.signals import post_save
from users.models import User
from .models import Connect
from users.models  import UserImage


def create_connect(sender, instance, created, **kwargs):
    if created:
        Connect.objects.create(user=instance)
        UserImage.objects.create(user=instance)
post_save.connect(create_connect,sender=User)

