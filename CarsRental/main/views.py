import random
import string
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")

def about(request):
    return HttpResponse("A simple paragraph about Car Rentals.")

def generate_password(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return HttpResponse(password)
