from django.urls import path
from . import views

app_name= "main"

urlpatterns = [
    path('', views.main_view, name="main"),
    path('about/' , views.about_view, name="about"),
    path('password/generate/', views.password_view ,name= "password" )

]