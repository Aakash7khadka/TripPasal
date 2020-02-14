from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from flight . models import airlines

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render(request,'home.html')

# Create your views here.
def homepage(request):
    
 
    plane=airlines.objects.order_by('price')[:5]

    
    return render(request,'home.html',{'plane':plane})


def hotel(request):
    return render(request,'hotel.html')

def addhotels(request):
    return render(request,'addhotel.html')

def flight(request):
    return render(request,'flight.html')