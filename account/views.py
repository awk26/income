from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from  django.contrib.auth import login, logout, authenticate
from .models import *

def home(request):
    return render(request,"home.html")


def register(request):
    if request.method=="POST":
        obj=UserCreationForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":UserCreationForm}
        return render(request,"form.html",d)
    
def loginn(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pswd=request.POST.get("pswd")
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            request.session["id"]=user.id
            print(request.session.get("id"))
            login(request,user)
            return redirect("/")
        else:
            d={"form":Loginform}
            return render(request,"form.html",d)
    else:
            d={"form":Loginform}
            return render(request,"form.html",d)
def logoutt(request):
    logout(request)
    return redirect("/")        
                
    


