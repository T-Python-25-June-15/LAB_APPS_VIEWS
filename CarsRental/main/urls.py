from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('',views.view_page, name="view_page"),
    path('about/', views.about_page, name="about_page"),
    path('password/generate',views.generate_password,name="generate_password")

]