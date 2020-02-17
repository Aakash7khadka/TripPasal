from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from hotels.models import hotels
from flight.models import airlines
from django.views.generic import ListView,DetailView
# Create your views here.

class HotelDetailSlugView(DetailView):
      queryset=hotels.objects.all()
      template_name="detail.html"
      def get_object(self,*args,**kwargs):
        request=self.request
        slug=self.kwargs.get('slug')
       
        try:
            instance=hotels.objects.get(slug=slug)
        except hotels.DoesNotExist:
            raise Http404("Not found....")
        except hotels.MultipleObjectsReturned:
            qs=hotels.objects.filter(slug=slug,active=True)
            instance=qs.first()
        except:
            raise Http404("Ummmm")
        
        return instance

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render(request,'home.html')

# Create your views here.
def homepage(request):
    
 
    plane=airlines.objects.order_by('price')[:5]

    cheaphotels=hotels.objects.order_by('?')[:5]
    return render(request,'home.html',{'plane':plane,'cheaphotels':cheaphotels})


def hotel(request):
    return render(request,'hotel.html')

def addhotels(request):
    return render(request,'addhotel.html')

def flight(request):
    return render(request,'flight.html')

def cityhotels(request):
    citi=request.POST.get('cityhotel', False)
    hotel=hotels.objects.all()
    if(citi=="kathmandu"):
        hotel=hotels.objects.filter(city="kathmandu")
        
    elif(citi=="pokhara"):
        hotel=hotels.objects.filter(city="pokhara")
    elif(citi=="biratnagar"):
        hotel=hotels.objects.filter(city="biratnagar")
    return render(request,"cityhotel.html",{'hotelcity':hotel,'city':citi})
'''
def all(request):
    hotel=hotels.objects.all()
    return render(request,"cityhotel.html",{'hotelcity':hotel})
def kathmandu(request):
    hotel=hotels.objects.all()
    return render(request,"cityhotel.html",{'hotelcity':hotel})
def pokhara(request):
    hotel=hotels.objects.all()
    return render(request,"cityhotel.html",{'hotelcity':hotel})
def biratnagar(request):
    hotel=hotels.objects.all()
    return render(request,"cityhotel.html",{'hotelcity':hotel})
    '''