from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Messaging,Connect
from users.models import User
from.serializers import MessagingSerializer,UserSerialzer
# Create your views here.
@api_view(['GET'])
def continous_chat(request,reciever,sender):
    recieved=Messaging.objects.filter(to__user__id=sender,by__user__id=reciever).order_by('-id')[0:1]
    sent=Messaging.objects.filter(by__user__id=sender,to__user__id=reciever).order_by('-id')[0:1]
    sent_serializer=MessagingSerializer(recieved,many=True)
    recieved_serializer=MessagingSerializer(sent,many=True)
    if sent_serializer or recieved_serializer ==True:
        return Response({"status":200,"message":"Got it","data":sent_serializer.data,"recieved":recieved_serializer.data})
    return Response({"status":404,"message":"Message not found","data":sent_serializer.data,'recieved':recieved_serializer.data})
@api_view(['GET'])
def get_message(request,reciever,sender):
    recieved=Messaging.objects.filter(to__user__id=sender,by__user__id=reciever)
    sent=Messaging.objects.filter(by__user__id=sender,to__user__id=reciever)
    sent_serializer=MessagingSerializer(recieved,many=True)
    recieved_serializer=MessagingSerializer(sent,many=True)
    if sent_serializer or recieved_serializer ==True:
        return Response({"status":200,"message":"Got it","data":sent_serializer.data,"recieved":recieved_serializer.data})
    return Response({"status":404,"message":"Message not found","data":sent_serializer.data,'recieved':recieved_serializer.data})
@api_view(['POST',"GET"])
def post_message(request):
    data=request.data   
    by=data['by']
    to=data['to']
    print(by,to)
    sender=Connect.objects.get(user_id=by).pk
    reciever=Connect.objects.get(user_id=to).pk
    data['by']=sender
    data["to"]=reciever
    serializer = MessagingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status":200,"message":"Your data was sent","data":serializer.data})
    else:
        return Response({"status":420,"message":"Error happened","data":serializer.errors})
@api_view(['GET'])
def get_user(request,id):
    queryset=User.objects.get(id=id)
    serialzer=UserSerialzer(queryset)
    return Response({'username':serialzer.data['username']})
def authenticate(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        users=User.objects.values("username","password")
        usernames=[users[i]["username"]for i in range(users.count())]
        passwords=[users[i]["password"]for i in range(users.count())]
        try:
            if usernames.index(username) >= 0:
                if passwords[usernames.index(username)]==password:
                    data_to_pass = {"username":username}
                    request.session['data'] = data_to_pass
                    return redirect('index')
                else:
                    context={'response':'Password Unmatched'}
                return render(request,"chat/auth.html",context)
        except ValueError:
            context={'response':'Username not found'}
            return render(request,"chat/auth.html",context)
    context={'response':'Please enter your credentials'}
    return render(request,"chat/auth.html",context)
def index(request):
    data_received = request.session.get('data', None)
    if data_received:
        username=data_received['username']
        user=User.objects.filter(username=username).values('id','username',)
        connected=Connect.objects.filter(user__username=username).values('friends__id','friends__username',)
        context={
            "user":user,
            "recievers":connected,
        }
        return render(request,"chat/index.html",context)
    else:
        return redirect('login/')
class UserView(generics.ListAPIView):
    queryset=User.objects.all()
    lookup_field='id'
    serializer_class=UserSerialzer
class MessagingView1(generics.ListAPIView,generics.CreateAPIView):
    queryset=Messaging.objects.all().order_by('-id')[:5]
    serializer_class= MessagingSerializer
class MessagingView2(generics.ListAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Messaging.objects.all().order_by('-id')[:5]
    lookup_field='id'
    serializer_class= MessagingSerializer

class ConnectView(APIView):
    def get(self,request):
        data=request.data
        username=data['username']
        list_obj=list(Connect.objects.filter(user__username=username).values_list('friends__username',flat=True))
        add_friends=User.objects.exclude(username__in=list_obj).exclude(username=username)
        friend_serializer=UserSerialzer(add_friends,many=True)
        return Response({"status":200,"message":"Got it","data":friend_serializer.data})
    def post(self,request):
        try: 
            data=request.data
            username=data['username']
            friend=data['friend']
            print(friend,username)
            user=User.objects.get(username=username)
            friend=User.objects.get(username=friend)
            user_connect=Connect.objects.get(user=user)
            user_connect.friends.add(friend)
            
        except Exception as e:
            print(e)
        return Response({"status":200,"message":"Friend added"})
    def delete(self,request):
        try:
            data=request.data
            username=data['username']
            friend=data['friend']
            user=User.objects.get(username=username)
            friend=User.objects.get(username=friend)
            user_connect=Connect.objects.get(user=user)
            user_connect.friends.remove(friend)
        except Exception as e:
            print(e)
        return Response({"status":200,"message":"Friend removed"})