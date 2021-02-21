from django.shortcuts import render , HttpResponse
from . import models

def articles_list(request):
    articles = models.Articles.objects.all().order_by("date")
    args = {"articles" : articles }
    return render(request , "articles_list.html" , args)


def articles_ditale(request , slug):
    return HttpResponse(slug)
