from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random
# Create your views here.
def home_view(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here. !"

    return HttpResponse(content)


def about_view(request:HttpRequest):

    content = "<h2> Car Rental, It is a system that enables customer to rent a car to place their choice online at any time at any place.</h2>"

    return HttpResponse(content)

def generate_password_view(request:HttpRequest):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=10))
    return HttpResponse(password)

