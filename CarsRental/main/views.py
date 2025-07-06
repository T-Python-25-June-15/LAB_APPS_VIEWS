from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
# Create your views here.
def home_view(request:HttpRequest):
    content = "<h2> Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h2>"

    return HttpResponse(content)

def about_view(request:HttpRequest):

    content = "<h2>A simple paragraph about Car Rentals.</h2>"

    return HttpResponse(content)

def generate_password(request):
    characters = string.ascii_letters + string.punctuation
    password = ''
    for i in range(10):
        password += random.choice(characters)
    return HttpResponse(password)

