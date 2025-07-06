from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random


def page_view(request : HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)


def page_about(request : HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def generate_password(request : HttpRequest):

    small_letters = "abcdefghijklmnopqrstuvwxyz"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = string.punctuation
    all_list = small_letters + capital_letters + digits +  symbols 
    
    lower = random.choice(small_letters)
    upper = random.choice(capital_letters)
    digit = random.choice(digits)
    symbol = random.choice(symbols)
    
    current_pass = lower + upper + digit + symbol 
    
    for i in range(6):
        current_pass += random.choice(all_list) 
    
    current_pass = list(current_pass)
    random.shuffle(current_pass)
    final_password = ''.join(current_pass)
    return HttpResponse(final_password)