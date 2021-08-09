from django.shortcuts import render, redirect
from todo import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages# Create your views here.

def user_registration(request):
    form=forms.RegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context={"form":form}
            return render(request,"registration.html", context)

    return render(request,"registration.html",context)
def home(request):
    return render(request,"home.html")
def user_signin(request):
    form=forms.LoginForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            # to check whether username and password is correct
            user=authenticate(request,username=username,password=password)
            #if authenticate a user instance will be passed
            if user:
                login(request,user) #call login function from auth
                return redirect("userhome")
            else:
                context={"form":form}
                return render(request, "login.html", context)
    return render(request,"login.html",context)
def signout(request):
    logout(request)
    return redirect("home")
def userhome(request):
    return render(request,"userhome.html")