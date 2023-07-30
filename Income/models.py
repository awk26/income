from django.db import models
from django.contrib.auth.models import User
from django import forms


class Income(models.Model):
    income=models.IntegerField()
    income_type=models.CharField(max_length=30)
    income_date=models.DateField()
    description=models.TextField(max_length=40)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='Income'


#class incomeform(forms.Form):
    #income=forms.IntegerField()
    #income_type=forms.CharField(max_length=30)
    #income_date=forms.DateField()
    #description=forms.CharField(widget=forms.Textarea)


class incomemodelform(forms.ModelForm):
    class Meta:
        model=Income
        fields=["income","income_type","income_date","description"]



