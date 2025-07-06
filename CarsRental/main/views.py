from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def home_view(request):
    content="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here"
    return HttpResponse(content)

def about(request):

    content="Car rentals provide a convenient way for people to access transportation without owning a vehicle. Whether traveling for business, vacation, or while waiting for car repairs, renting a car offers flexibility and freedom. Customers can choose from various vehicle types based on their needs, such as economy cars, SUVs, or luxury models. Most rental companies offer daily, weekly, or monthly plans, making it easy to find an option that fits any budget or schedule."
    return HttpResponse(content)