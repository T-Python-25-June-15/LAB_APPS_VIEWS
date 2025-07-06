from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
# Create your views here.

def home_view(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)


def password_generate(request:HttpRequest):
    randompass = string.digits + string.ascii_letters + string.punctuation
    password_length = 10
    password = ""
    for i in range(password_length):
        password += random.choice(randompass)

    return HttpResponse(password)

def password_view(request:HttpRequest):
    """I added this one so when the user go to password page it would tell him to go generate"""
    content = "Go to password/generate/ to generate a random password"
    return HttpResponse(content)