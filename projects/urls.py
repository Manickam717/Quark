from django.urls import path
from . import views

urlpatterns = [
    path( "add_project" ,views.add_project ) , 
    path( "enroll_project" ,views.enroll_project) ,
]
