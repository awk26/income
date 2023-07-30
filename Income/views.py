from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth.models import User


def addincome(request):
    if request.method == "POST":
        # income=request.POST.get("income")
        # income_type=request.POST.get("income_type")
        # income_date=request.POST.get("income_date")
        # description=request.POST.get("description")
        # user_id=request.session.get("id")
        # obj_user=User.objects.get(id=user_id)
        # obj=Income()
        # obj.income=income
        # obj.income_type=income_type
        # obj.income_date=income_date
        # obj.description=description
        # obj.user=obj_user
        user_id = request.session.get("id")
        obj_user = User.objects.get(id=user_id)
        obj=incomemodelform(request.POST)
        data=obj.save(commit=False)
        data.user=obj_user
        obj.save()
        return redirect("/")
    else:
        #d = {"form": incomeform}
        d={"form":incomemodelform}
        return render(request, "form.html", d)


def details(request):
    obj = Income.objects.all()
    d = {'data': obj}
    return render(request, "details.html", d)


def delete(request, incid):
    obj = Income.objects.get(id=incid)
    obj.delete()
    return redirect("/Inc-details")


def edit(request, incid):
    data = Income.objects.get(id=incid)
    if request.method == "POST":
        obj = incomemodelform(request.POST, instance=data)
        obj.save()
        return redirect("/")
    else:
        d = {"form": incomemodelform(instance=data)}
        return render(request, "form.html", d)
