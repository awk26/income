from django.shortcuts import render, redirect
from .models import *

def addexpense(request):
    if request.method=="POST":
        obj=expenseform(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":expenseform}
        return render(request,"form.html",d)

def details(request):
    obj=Expense.objects.all()
    d={'data1':obj}
    return render (request,"details1.html",d)



def delete(request,incid):
    obj=Expense.objects.get(id=incid)
    obj.delete()
    return redirect("/Inc-details")

def edit(request,incid):
    data=Expense.objects.get(id=incid)
    if request.method=="POST":
        obj=expenseform(request.POST,instance=data)
        obj.save()
        return redirect("/")
    else:
        d={"form":expenseform(instance=data) }
        return render(request,"form.html",d)            
