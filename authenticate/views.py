from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

redirect_url = "stack:ask"
message = " have an account"

def empty(request):
    if request.user.is_authenticated:
        return redirect(reverse(redirect_url))
    return redirect(reverse("authenticate:login"))

def signup_user(request):
    if request.user.is_authenticated:
        return redirect(reverse(redirect_url))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse(redirect_url))
        except Exception:
            messages.add_message(request, messages.ERROR, "your username is already taken")
    return render(request, "auth.html", context={"title":"Signup", "message": message ,"final":"login", "login":False})

def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse(redirect_url))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse(redirect_url))
        else:
            messages.add_message(request, messages.ERROR, "your username or password is incorrect")

    return render(request, "auth.html", context={"title":"Login", "message": "don't " + message, "final": "signup", "login": True})


