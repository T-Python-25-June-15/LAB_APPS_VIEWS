from django.urls import path
from . import views

main="main"

urlpatterns = [
    path("",views.page_view , name="page_view"),
    path("about/",views.about_view, name="about_view"),
    path("password/generate/",views.genratePassword_view, name="genratePassword_view")
]
