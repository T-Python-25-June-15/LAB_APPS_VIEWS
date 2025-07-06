from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import random
import string

x = ["awd","wfaf","Gegg"]

def default_page(response:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_page(response:HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def random_pass(response:HttpRequest):

    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=10))

    content = f"{password}"
    return HttpResponse(content)