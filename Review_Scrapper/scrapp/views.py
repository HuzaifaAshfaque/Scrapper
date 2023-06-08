from django.shortcuts import render,HttpResponse
from scrapp.models import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

# Create your views here.
def index(request):
    
    crev = card.objects.all().order_by('-id')[0:6]
    mydict = {"card":crev}
    return render(request,"index.html",context= mydict)

# ------------------------------------------------------------------------------

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

# -------------------------------------------
def review(request):
    if request.method == 'POST':
        try:
            searchString= request.POST.get('input_data')
            searchString=  searchString.replace(" ","")
            print(searchString)
            history = Search(s_query= searchString)
            history.save()
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()

            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            # print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    #name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

                except:
                    name = 'No Name'

                try:
                    #rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text


                except:
                    rating = 'No Rating'

                try:
                    #commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                    
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    #custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ",e)

                print("what doees ???")
                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)
                # for x in reviews:
                #     print(x)
            return render( request, 'review.htm',context={'reviews':reviews})
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'


    else:
        return render(request,'review.htm')
    
# ----------------------------------------------------------------------------

def donateus(request):
    return render(request,"donateus.html")
 