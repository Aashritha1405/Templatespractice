from django.shortcuts import render,redirect
from .models import TODO
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        data=User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'),email=request.POST.get('email'))
            
        return redirect('login')
    return render(request,'signup.html')
    

def login_view(request):
    if request.method == "POST":
        user=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user is None:
            return HttpResponse("user mot found")
        login(request, user)
        return redirect("create")
        
        
    return render(request,'login.html')

@login_required
def get_user(request):
    return HttpResponse({"data":"data"})

def logout(request):
    logout(request)
    return redirect('login')
    
def create(request):
    if request.method == "POST":
        
        title=request.POST.get('title')
        status=request.POST.get('status')
        data=TODO.objects.create(user=request.user,title=title,status=status)
        data.save()
        return redirect("todo")
    return render(request,'create.html')

def todo(request):
    todos=TODO.objects.all()
    print(TODO.objects.values())
    context={"data":todos}
    return render(request,"todo.html",context)

def update(request,id):
    data=TODO.objects.get(id=id)
    if request.method=="POST":
        
        data.title=request.POST.get('title')
        data.status=request.POST.get('status')
        data.save()
        
        return redirect("todo")
    context={"data":data}   
    return render(request,"update.html",context)
        
def delete(request,id):
    todo=TODO.objects.get(id=id)
    todo.delete()
    return redirect("todo")
        
        
        
        
    