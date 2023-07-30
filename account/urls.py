from django.urls import path
from .import views as v


urlpatterns = [
    path("reg",v.register,name="register"),
    path("login", v.loginn,name="login"),
    path("logout", v.logoutt,name="logout")    
]