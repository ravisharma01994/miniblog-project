from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignForm,LoginForm,change_pss,PostForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash,authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        us=request.user
        full_name=us.get_full_name()
        gps=us.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'fname':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

def sign_up(request):
    if request.method=='POST':
        fm=SignForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Wow!! You have registered Now.')
            us=fm.save()
            gp=Group.objects.get(name='Author')
            us.groups.add(gp)
            fm=SignForm()
    else:
        fm=SignForm()
    return render(request,'blog/signup.html',{'fm':fm})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def log_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=LoginForm()
        return render(request,'blog/login.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def chg_pwd(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=change_pss(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return HttpResponseRedirect('/dashboard/')
        else:
            form=change_pss(user=request.user)
        return render(request,'blog/change.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pf=PostForm(request.POST)
            if pf.is_valid():
                title=pf.cleaned_data['title']
                desc=pf.cleaned_data['desc']
                form=Post(title=title,desc=desc)
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pf=PostForm()
        return render(request,'blog/addpost.html',{'pf':pf})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request,id):
    if request.user.is_authenticated:
        pi=Post.objects.get(pk=id)
        if request.method=='POST':
            pf=PostForm(request.POST,instance=pi)
            if pf.is_valid():
                pf.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pf=PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'pf':pf})
    else:
        return HttpResponseRedirect('/login/')
    
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            dl=Post.objects.get(pk=id)
            dl.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')