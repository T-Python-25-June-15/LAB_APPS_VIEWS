from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_view(request:HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content = "A simple paragraph about Car Rentals. "
    return HttpResponse(content)


import random

def shuffel(password:str, n):
    if n == 0:
        return password
    new_password = ''
    x = int(random.random() * len(password))
    for i in range(len(password)):
        if i == x:
            continue
        new_password += password[i]
    
    new_password += password[x]     
      
    return shuffel(new_password, n-1)

def generate_password():
    numbers = '1234567890'
    small_chars = "qwertyuiopasdfghjklzxcvbnm"
    capital_chars = "QWERTYUIOPASDFGHJKLZXCVBNM"
    x = "!@#$%^&*??"
    
    new_password = ""
    for i in range(3):
        new_password += str(small_chars[(int(random.random() * 26))])
        new_password += str(capital_chars[(int(random.random() * 26))])
        
    for i in range(2):
        new_password += str(numbers[(int(random.random() * 10))])
        new_password += str(x[(int(random.random() * 10))])
    
    return shuffel(new_password, 10)
    
def password_generate_view(request:HttpRequest):
    new_password = generate_password()
    return HttpResponse(new_password)