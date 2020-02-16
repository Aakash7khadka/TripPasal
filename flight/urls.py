from django.urls import path

from . import views

urlpatterns=[
    
    path('compare_flight',views.showflight,name='showflight'),
    path('show_flight',views.show_flight,name='show_flight'),
]