import random
import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def view_page(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_page(request:HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)


def generate_password(request:HttpRequest):
    length = 10
    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(all_chars)

    return HttpResponse(password)