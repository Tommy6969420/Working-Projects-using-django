from rest_framework import serializers
from.models import Messaging,Connect, User
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=['id','password']
class MessagingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Messaging
        fields="__all__"
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=['id','password']
class ConnectSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Connect
        exclude=['id','password']
