from django.urls import path,re_path
from . import views
from . views import HotelDetailSlugView



urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('hotels/',views.hotel,name="hotels"),
    path('flight/',views.flight,name="flight"),
    path('logout/',views.logout,name="logout"),
    path('addhotels/',views.addhotels,name='addhotels'),
    re_path('view/(?P<slug>[\w-]+)/$',HotelDetailSlugView.as_view(),name='HotelDetailSlugView'),
    
    
]