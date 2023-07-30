from django.urls import path
from .import views as v


urlpatterns = [
     path("add",v.addincome,name="addincome"),
     path("details",v.details,name="incdetails"),
     path("del/<int:incid>",v.delete,name="delete"),
     path("edit/<int:incid>",v.edit,name="edit")     
]