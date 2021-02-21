from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/" , views.about),
    path("" , views.home),
    path("articles/" , include("articles.urls"))
]

urlpatterns += staticfiles_urlpatterns()
