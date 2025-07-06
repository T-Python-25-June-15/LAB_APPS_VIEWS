from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def about(request):
    return HttpResponse("A simple paragraph about Car Rentals.")



def generate_password(request):
    length = 10
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(all_characters)
    return HttpResponse(password)

