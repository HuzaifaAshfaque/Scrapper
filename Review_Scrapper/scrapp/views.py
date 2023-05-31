from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    
    return render(request,"index.html")

def aboutus(request):
    return render(request,"aboutus.html")

def review(request):
    return render(request,"review.htm")

def donate(request):
    return render(request,"donate.htm")
