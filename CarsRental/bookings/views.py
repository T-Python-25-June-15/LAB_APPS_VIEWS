from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

# Create your views here.

def home_view(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  !" \
    " we're excited to welcome you here."

    return HttpResponse(content)

def about_view(request:HttpRequest):

    content = "<h2>A simple paragraph about Car Rentals.</h2>"

    return HttpResponse(content)

def password_generate_view(request:HttpRequest):
    def generate_password(length=12):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        symbols = '!@#$%^&*()-_=+'
        all_chars = letters + letters.upper() + digits + symbols

        password = ''
        for _ in range(length):
            password += random.choice(all_chars)

        return password

    print(generate_password())

    content = f"<h2>{generate_password} </h2>"

    return HttpResponse(content)