from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

def home_view(req:HttpRequest):
    message ="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(message)

def about_view(req:HttpRequest):
    message= "A simple paragraph about Car Rentals."
    return HttpResponse(message)

def password_generator_view(req:HttpRequest):
    password = passGenerate()
    return HttpResponse(password)


def passGenerate():
    chars = 'ABCDEFGHIJKMLNOPQRSTUVWXYZabcdevjhigklmnopqrstuvwxyz1234567890!@#$%&*'
    return random.choices(chars, k=10)