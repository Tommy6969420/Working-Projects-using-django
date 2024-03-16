from django.shortcuts import render, redirect
from.forms import UserForm, PostForm
from.models import Post,User,UserImage
from django.core.exceptions import ObjectDoesNotExist
from chat.models import Connect
# from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return render(request,'users/welcome.html')

def index(request):
    if request.method=="POST":
        print("hello mf")
        form=UserForm(request.POST)
        username=request.POST.get("username")
        gender=request.POST.get("gender")
        full_name=request.POST.get("full_name")
        date_of_birth=request.POST.get("date_of_birth")
        print(username,gender,full_name,date_of_birth,)
        if form.is_valid():
            username=request.POST.get("username")
            form.save()
            return redirect('homepip',username)
        else:
            form=UserForm()
            msg="form validation error please refill the form, tips:make sure youre using your own information"
            context={
        'form':form,
        'msg':msg
    }
            return render(request,'users/signup.html',context)

    form=UserForm()
    context={
        'form':form,
    }
    return render(request,'users/signup.html',context)
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        users=User.objects.values("username","password")
        # print(users.count())
        usernames=[users[i]["username"]for i in range(users.count())]
        passwords=[users[i]["password"]for i in range(users.count())]
        try:
            if usernames.index(username) >= 0:
                if passwords[usernames.index(username)]==password:
                    data_to_pass = {"username":username,"password":password}
                    request.session['data'] = data_to_pass
                    return redirect('home',username)
                else:
                    context={'response':'Password Unmatched'}
                    return render(request,"users/login.html",context)
        except ValueError:
            context={'response':'Username not found'}
            return render(request,"users/login.html",context)
            print(passwords)
    context={'response':'Please enter your credentials'}
    return render(request,"users/login.html",context)
def home(request,username):
    data_received = request.session.get('data', None)
    if data_received:
        users=User.objects.values("username","password")
        # print(users.count())
        usernames=[users[i]["username"]for i in range(users.count())]
        try:
            if usernames.index(username) >= 0:
                pass
        except ValueError:
            context={'response':'Login is required for futher operations'}
            return redirect('login') 
        if request.method=="POST":
            print('progressing')
            description=request.POST.get('description')
            image=request.FILES.get('image')
            author=User.objects.get(username=username)
            Post(author=author,image=image,description=description).save()
            posts=Post.objects.all()
            form=PostForm()
            context={
                'name':username,
                "posts":posts,
                'form':form
            }
            print("Saving Image")
            return render(request,'users/home.html',context)
        posts=Post.objects.all()
        form=PostForm()
        friends=Connect.objects.filter(user__username=username).values('friends__username')
        context={
            'name':username,
            "posts":posts,
            'form':form,
            'friends':friends
        }
        return render(request,'users/home.html',context)
    
    else:
        return redirect('login')
def profile(request,username):
    if request.method=="post":
        pass
    try:
        user=User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect("login")
    try:
        profile_photo=UserImage.objects.get(user=user)
    except UserImage.DoesNotExist:
        gender=user.gender
        if user.gender=="male":
            user_image=UserImage(user=user,image="profiles/male-avatar.jpg")
            user_image.save()
        elif user.gender=="female":
            user_image=UserImage(user=user,image="profiles/female-avatar.jpg")
            user_image.save()
        else:
            user_image=UserImage(user=user,image="profiles/others-avatar.jpg")
            user_image.save()
                       
        profile_photo=UserImage.objects.get(user=user)
    user_posts=Post.objects.filter(author=user)
    context={
            "user":user,
            "photo":profile_photo,
            'posts':user_posts
        }
    return render(request,'users/profile.html',context)

def friends(request):
    data_received = request.session.get('data', None)
    if data_received:
        username=data_received['username']
        try:
            user=User.objects.get(username=username)
            list_obj=list(Connect.objects.filter(user__username=username).values_list('friends__username',flat=True))
            friends=Connect.objects.filter(user__username=username).values('friends__username')
            add_friends=User.objects.exclude(username__in=list_obj).exclude(username=username)
            friends__obj=list(friends.values_list('friends__username',flat=True))
            print(friends__obj)
            req_friends=Connect.objects.filter(friends__username=username).exclude(user__username__in=friends__obj).values('user__username')
            print(req_friends)
            context={
                "user":user,
                "friends":friends,
                'add_friends':add_friends,
                'req_friends':req_friends
            }
            return render(request,'users/friends.html',context)
        except User.DoesNotExist:
            return redirect("login")
    return redirect("login")    