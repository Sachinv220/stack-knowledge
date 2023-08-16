from django.urls import path 
from . import views


app_name = "authenticate"

urlpatterns = [
    path("", views.empty, name="base"), 
    path("login/", views.login_user, name="login"), 
    path("signup/", views.signup_user, name="signup"), 
]
