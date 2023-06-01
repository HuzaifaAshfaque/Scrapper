from django.shortcuts import render,HttpResponse
from scrapp.models import *

# Create your views here.
def index(request):
    crev = card.objects.all().order_by('-id')[0:6]
    mydict = {"card":crev}
    return render(request,"index.html",context= mydict)

def aboutus(request):
    return render(request,"aboutus.html")

def review(request):
    return render(request,"review.htm")

def donate(request):
    return render(request,"donate.htm")
