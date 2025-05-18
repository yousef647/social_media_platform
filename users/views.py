from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import UserRegistrationForm
from users.factories import ProfileFactory

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ProfileFactory.create_profile(user, form.cleaned_data["role"])
            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")