from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import random
import string

x = ["awd","wfaf","Gegg"]

def default_page(response:HttpRequest):
    content = "hello world"
    return HttpResponse(content)

def about_page(response:HttpRequest):
    content = "hello world about page"
    return HttpResponse(content)

def random_pass(response:HttpRequest):

    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=10))

    content = f"{password}"
    return HttpResponse(content)