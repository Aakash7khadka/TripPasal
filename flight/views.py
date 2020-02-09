from django.shortcuts import render
from . models import airlines

# Create your views here.
def showflight(request):
    first_dest=request.POST['first_dest']
    second_dest=request.POST['second_dest']
    first_time=int(request.POST['first_time'])
    second_time=int(request.POST['second_time'])
    ft=first_time
    st=second_time
    plane=airlines.objects.filter(source=first_dest).filter(destination=second_dest).order_by('price').filter(departure_time__gte=first_time).filter(departure_time__lte=second_time)

    return render(request,"flightcomp.html",{'plane':plane})


    
