from django.urls import path
from .import views as v


urlpatterns = [
     path("add",v.addexpense,name="addexpense"), 
     path("details",v.details,name="expdetails"), 
      path("del/<int:incid>",v.delete,name="delete"),
     path("edit/<int:incid>",v.edit,name="edit")   
]