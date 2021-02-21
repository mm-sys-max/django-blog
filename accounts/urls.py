from . import views
from django.urls import path



app_name = "accounts"

urlpatterns = [
    path("signup" , views.sign_up , name="signup")
]