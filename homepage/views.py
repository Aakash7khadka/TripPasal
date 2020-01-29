from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')


def hotel(request):
    return render(request,'hotel.html')



def flight(request):
    return render(request,'flight.html')