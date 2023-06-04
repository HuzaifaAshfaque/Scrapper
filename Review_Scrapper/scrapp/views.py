from django.shortcuts import render,HttpResponse
from scrapp.models import *
from datetime import datetime

# Create your views here.
def index(request):
    
    crev = card.objects.all().order_by('-id')[0:6]
    mydict = {"card":crev}
    return render(request,"index.html",context= mydict)

def aboutus(request):
    status = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today()) 
        contact.save()
        status = True

    msg = {"m":status}
    return render(request,"aboutus.html",context=msg)

def review(request):
    return render(request,"review.htm")

def donate(request):
    return render(request,"donate.htm")
 