from django.db import models

from django import forms

class Loginform(forms.Form):
    uname=forms.CharField(max_length=30,label="username")
    pswd=forms.CharField(max_length=30,label="password")
