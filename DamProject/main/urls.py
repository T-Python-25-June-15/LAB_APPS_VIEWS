from . import views
from django.urls import path

app_name = "dam"

urlpatterns = [
    path('password/generate', views.random_pass),
    path('about/', views.about_page),
    path('', views.default_page),
]
