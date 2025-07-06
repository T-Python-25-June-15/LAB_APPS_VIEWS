from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("",views.page_view, name="page_view"),
    path("about/",views.page_about, name="page_about"),
    path("password/generate/",views.generate_password, name="generate_password")

    ]