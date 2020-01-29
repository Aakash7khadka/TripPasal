from django.urls import path,re_path
from . import views
from . views import homepage

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('',views.hotel,name="hotel"),
    path('',views.flight,name="flight"),
]