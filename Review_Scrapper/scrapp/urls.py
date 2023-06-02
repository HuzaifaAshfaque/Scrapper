from django.contrib import admin
from django.urls import path
from scrapp import views

urlpatterns = [
    path("",views.index,name='home'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("reviews",views.review,name='reviews'),
    path("donate",views.donate,name='donate')

]