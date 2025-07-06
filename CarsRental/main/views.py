from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
import random
import string
# Create your views here.

def main_view(request: HttpRequest):
    content= "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(requst: HttpRequest):
    content= "A simple paragraph about Car Rentals. "
    return HttpResponse(content)

def password_view(rewust: HttpRequest):
    password= randomly_password_generated()


    return HttpResponse(password)

def randomly_password_generated():
    pass_length= 10
    password =""
    all_lower_characters = list(string.ascii_lowercase)
    all_upper_characters = list(string.ascii_uppercase)
    all_digit = list(string.digits)
    all_symbols = list(string.punctuation)

    result = all_lower_characters + all_upper_characters + all_digit + all_symbols

    for i in range(pass_length):
        password += random.choice(result)

    return password


