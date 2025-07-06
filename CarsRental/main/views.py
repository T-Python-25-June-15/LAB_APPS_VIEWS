from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.
def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request : HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def password_view(request : HttpRequest):
    myrange = string.digits + string.ascii_letters + string.punctuation
    password = ""
    for i in  range (10):
        password = password + random.choice(myrange)
    return HttpResponse(password)
        
    
    


