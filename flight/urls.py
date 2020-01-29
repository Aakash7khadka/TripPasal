from django.urls import path

from . import views

urlpatterns=[
    
    path('compare_flight',views.showflight,name='showflight')
]