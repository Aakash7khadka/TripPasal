import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from django.shortcuts import render
from . models import hotels
# Create your views here.

def addnewhotels(request):
    getcity=request.GET['destination']
    my_url="https://www.oyorooms.com/np/hotels-in-pokhara"

    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")

    #grab all the room container
    containers=page_soup.findAll("div",{"class":"oyo-row oyo-row--no-spacing hotelCardListing"})

    #for container in containers:
    container=containers[0]
    title=container.h3["title"]
    price_container=container.findAll("span",{"class":"listingPrice__finalPrice"})
    price=price_container[0].text
    price=price.replace("NPR","")
    street_container=container.findAll("span",{"class":"u-line--clamp-2"})
    street=street_container[0].text
    img_container=container.findAll("img",{"class":"listingImageCard__carousel__imgWrapper listingImageCard__carouselImg"})   
    img=img_container[0]["src"]
    rating_container=container.findAll("meta",{"itemprop":"ratingValue"})
    rating=rating_container[0]["content"]
    latitude_container=container.findAll("meta",{"itemprop":"latitude"})
    latitude=latitude_container[0]["content"]
    longitude_container=container.findAll("meta",{"itemprop":"longitude"})
    longitude=longitude_container[0]["content"]
    hotel=hotels(city=getcity,price=price,street=street,latitude=latitude,longitude=longitude,ratings=rating,hotel_title=title,image=img)
    hotel.save()
    print(hotel)

    
    return render(request,"addhotelsucessful.html")

