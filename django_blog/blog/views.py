# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Posts
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from . import models
def signup(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        email=request.POST.get('uemail')
        password=request.POST.get('upassword')
        new_user=User.objects.create_user(username=name,email=email,password=password)
        new_user.save()
        return redirect('/login')

    return render(request, 'blog/signup.html')

def login(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        password=request.POST.get('upassword')
        userr=authenticate(request,username=name,password=password)
        if userr is not None:
            auth_login(request,userr)
            return redirect('/home')
        else:
            return redirect('/login')

    return render(request,'blog/login.html')
# blog/views.py
@login_required(login_url='/login/')  
def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Posts(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')  
    return render(request, 'blog/new_post.html')

def my_posts(request):
    context={
        'posts':Posts.objects.filter(author=request.user)
    }
    return render(request, 'blog/my_posts.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    context={
        'posts':Posts.objects.all()
    }
    return render(request, 'blog/home.html',context)
