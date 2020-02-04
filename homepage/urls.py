from django.urls import path,re_path
from . import views
from . views import homepage


urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('hotel/',views.hotel,name="hotel"),
    path('flight/',views.flight,name="flight"),
    path('logout/',views.logout,name="logout")
    
]