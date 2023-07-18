from django.contrib import admin
from django.urls import path
from scrapp import views

urlpatterns = [
    path("",views.index,name='home'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("review",views.review,name='reviews'),


]