from django.urls import path,re_path

from . import views

urlpatterns=[
    
    path('add',views.addnewhotels,name='addnewhotels'),
    path('addtrivago',views.addnewhotels_trivago,name='addnewhotels_trivago'),
    
]