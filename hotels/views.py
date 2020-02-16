import bs4

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from django.shortcuts import render
from . models import hotels
import time


def addnewhotels(request):
    getcity=request.GET['destination']
    if(getcity.lower()=="kathmandu"):
        oyo_ktm(getcity)
    elif(getcity.lower()=="pokhara"):
        oyo_pkra(getcity)

    
    return render(request,"addhotelsucessful.html")

def oyo_pkra(getcity):
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
    try:
        rating=rating_container[0]["content"]
    except:
        rating=0
    latitude_container=container.findAll("meta",{"itemprop":"latitude"})
    latitude=latitude_container[0]["content"]
    longitude_container=container.findAll("meta",{"itemprop":"longitude"})
    longitude=longitude_container[0]["content"]
    hotel=hotels(city=getcity,price=price,street=street,latitude=latitude,longitude=longitude,ratings=rating,hotel_title=title,image=img)
    hotel.save()
    
def oyo_ktm(getcity):
    
    my_url="https://www.oyorooms.com/np/hotels-in-kathmandu/"

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
    try:
        rating=rating_container[0]["content"]
    except:
        rating=0
    latitude_container=container.findAll("meta",{"itemprop":"latitude"})
    latitude=latitude_container[0]["content"]
    longitude_container=container.findAll("meta",{"itemprop":"longitude"})
    longitude=longitude_container[0]["content"]
    hotel=hotels(city=getcity,price=price,street=street,latitude=latitude,longitude=longitude,ratings=rating,hotel_title=title,image=img)
    hotel.save()

def addnewhotels_trivago(request):
    getcity=request.GET['destination']
    if(getcity.lower()=="kathmandu"):
        trivago_ktm(getcity)
    elif(getcity.lower()=="pokhara"):
        trivago_pkra(getcity)

    
    return render(request,"addhotelsucessful.html")

def trivago_ktm(getcity):
    for x in range(0,5):
        url="https://www.trivago.com/?aDateRange%5Barr%5D=2020-02-24&aDateRange%5Bdep%5D=2020-02-25&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=66151%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=16093&address=&addressGeoCode=&offset="+str(x)+"&ra=&settingsChanged=currency"

        driver=webdriver.Firefox()

        driver.get(url)
        scheight = .1
        while scheight < 9.9:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
            scheight += .01
        time.sleep(5)

        html=driver.execute_script("return document.documentElement.outerHTML")
        web_soup=bs(html,'html.parser')
        web_soup=list(web_soup)
        web_soup=web_soup[0]
        block_container=web_soup.findAll("li",{"class","hotel-item item-order__list-item js_co_item"})

        for container in block_container:
            try:    
                image_container=container.findAll("img",{"class":"lazy-image__image item__image item__image--has-gallery"})
                image=image_container[0]["src"]
                image=image.replace("'","")
                
                title_container=container.findAll("span",{"class","item-link name__copytext"})
                title_container=title_container[0]
                title=title_container.text
                
                price_container=container.findAll("span",{"class":"accommodation-list__price--e36d7 accommodation-list__price--46666"})
                price_container=price_container[0]
                price=price_container.text
                price=price.replace("$","")
                price=float(price)*114.08
                
                address_container=container.findAll("p",{"class":"details-paragraph details-paragraph--location location-details"})
                address_container=address_container[0]
                address=address_container.text
                address=address.replace("'","")
                ratings_container=container.findAll("span",{"class":"item-components__pillValue--c1d5b item-components__value-sm--78854 item-components__pillValue--c1d5b"})
                ratings_container=ratings_container[0]
                ratings=ratings_container.text
                ratings=float(ratings)
                ratings/=2
                latitude=""
                longitude=""
                hotel=hotels(city=getcity,price=price,street=address,latitude=latitude,longitude=longitude,ratings=ratings,hotel_title=title,image=image)
                hotel.save()
            except:
                continue   
    

def trivago_pkra(getcity):
    url="https://www.trivago.com/?aDateRange%5Barr%5D=2020-03-09&aDateRange%5Bdep%5D=2020-03-10&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=66170%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=16093&address=&addressGeoCode=&offset=0&ra="

        
    driver=webdriver.Firefox()

    driver.get(url)
    html=driver.execute_script("return document.documentElement.outerHTML")
    web_soup=bs(html,'html.parser')
    web_soup=list(web_soup)
    web_soup=web_soup[0]
    block_container=web_soup.findAll("li",{"class":"hotel-item item-order__list-item js_co_item"})
    
    container=block_container[0]
    image_container=container.findAll("img",{"class":"lazy-image__image item__image item__image--has-gallery"})
    image=image_container[0]["src"]
    image=image.replace("'","")
    print(image)
    title_container=container.findAll("span",{"class","item-link name__copytext"})
    title_container=title_container[0]
    title=title_container.text
    print(title)

    price_container=container.findAll("strong",{"data-qa":"recommended-price"})
    try:
            
        price_container=price_container[0]
        price=price_container.text
        price=price.replace("$","")
    except:
        price=9999999    
    address_container=container.findAll("p",{"class":"details-paragraph details-paragraph--location location-details"})
    address_container=address_container[0]
    address=address_container.text
    address=address.replace("'","")
    ratings_container=container.findAll("span",{"class":"item-components__pillValue--dae73 item-components__value-sm--e8adb item-components__pillValue--dae73"})
    try:
        ratings_container=ratings_container[0]
    
        ratings=ratings_container.text
        ratings=float(ratings)
        ratings/=2
    except:
        ratings=0    
    latitude=""
    longitude=""
    hotel=hotels(city=getcity,price=price,street=address,latitude=latitude,longitude=longitude,ratings=ratings,hotel_title=title,image=image)
    hotel.save()