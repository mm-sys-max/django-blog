from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    # return HttpResponse("html")
    return render(request , "home.html")

def about(request):
    # return HttpResponse("ops we dont have bio ... ")
    return render(request , "about.html")
