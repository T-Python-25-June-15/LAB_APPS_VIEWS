from . import views
from django.urls import path

app_name= "main"

urlpatterns= [
    path('', views.home_view, name="home_view"),
    path('about/', views.about_view, name="about_view"),
    path('password/generate/', views.password_generator_view, name="password_generator"),
]