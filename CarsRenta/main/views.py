from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import string
import random


def page_view(request:HttpRequest):
    content = " Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here. "
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content = " A simple paragraph about Car Rentals.  "
    return HttpResponse(content)


def genratePassword_view(request:HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = ''.join(random.choices(characters,k=10))
    return HttpResponse(passwords)