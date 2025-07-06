from django.http import HttpResponse , HttpRequest
from django.shortcuts import render
import random

# Create your views here.

def home_view(request):
    
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    
    return HttpResponse(content)


def about_view(request):
    
    content = "A simple paragraph about Car Rentals."
    
    return HttpResponse(content)

def generate_password_view(response) : 
        
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()'
    
    all_chars = letters + numbers + symbols
    password = ''

    for i in range(10):
        password = password + random.choice(all_chars)
    return HttpResponse(password)

    
