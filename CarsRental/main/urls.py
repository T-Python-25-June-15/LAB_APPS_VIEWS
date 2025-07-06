from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('about/', views.about_view, name="about_view"),
    #path('password/',views.password_view,name="password_view"), i added this so when the user go to password page it tell him to go to generate
    path('password/generate/', views.password_generate, name="password_generate"),
]
