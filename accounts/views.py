from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login



def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    args = {"form":form}
    return render(request , "signup.html" , args)

def log_in(request):
    if request.method == "POST":
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           user = form.get_user()
           login(request , user)
           return redirect("articles:list")
    else:
        form = AuthenticationForm()
    args = {"form":form}
    return render(request , "login.html" , args)
