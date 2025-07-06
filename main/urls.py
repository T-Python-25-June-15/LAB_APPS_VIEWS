

from django.urls import path
from . import views as main


app_name = 'main'


urlpatterns = [
    path("", main.home_view, name="home_view"),
    path("about/", main.about_view, name="about_view"),
    path('password/generate/', main.password_generate_view, name="password_view"),
]
