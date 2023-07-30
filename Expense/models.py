from django.db import models
from django import forms
from django.contrib.auth.models import User

class Expense(models.Model):
    expense=models.IntegerField()
    expense_type=models.CharField(max_length=30)
    expense_date=models.DateField()
    description=models.TextField(max_length=40)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="expense"


class expenseform(forms.ModelForm):
    class Meta:
        model=Expense
        fields="__all__"



