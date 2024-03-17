from django.urls import path
from login_reg import views

urlpatterns = [
    path('' ,views.login ,name = 'login_page' ) , 
    path('Register' ,views.register ,name = 'registration_name' )
]