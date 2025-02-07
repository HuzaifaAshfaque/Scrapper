from django.shortcuts import render,HttpResponse
from scrapp.models import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import traceback , certifi ,ssl

# Create your views here.
def index(request):
    
    
    crev = card.objects.all().order_by('-id')[0:3]
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
            # Get search input
            searchString = request.POST.get('input_data', '').replace(" ", "")
            print(searchString)

            # Save search history
            history = Search(s_query=searchString)
            history.save()

            # Construct Flipkart URL
            flipkart_url = f"https://www.flipkart.com/search?q={searchString}"
            print(flipkart_url)

            # Fetch Flipkart page
            uClient = uReq(flipkart_url, cafile=certifi.where())
            flipkartPage = uClient.read()
            uClient.close()

            # Parse HTML
            flipkart_html = bs(flipkartPage, "html.parser")
            # print(flipkart_html)
            bigboxes = flipkart_html.findAll("div", {"class": "cPHDOP col-12-12"})
            del bigboxes[:3]

            # Extract first product details
            if not bigboxes:
                return HttpResponse("No products found", status=404)

            # print(bigboxes)

            box = bigboxes[0]
            # print(box)
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink, headers={'User-Agent': 'Mozilla/5.0'})
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            # print(prod_html)

            # Get reviews
            commentboxes = prod_html.find_all('div', {'class': "EPCmJX"})
            print(type(commentboxes))
            print(commentboxes[0])
            # print(commentboxes)
            reviews = []

            for commentbox in commentboxes:
                try:
                    name_tag = commentbox.find('p', {'class': '_2NsDsF AwS1CA'})
                    name = name_tag.text if name_tag else 'No Name'
                except:
                    name = 'No Name'

                try:
                    rating = commentbox.div.div.text
                except:
                    rating = 'No Rating'

                try:
                    commentHead_tag = commentbox.find('p', {'class': 'z9E0IG'})
                    commentHead= commentHead_tag.text if commentHead_tag else "No Comments"
                except:
                    commentHead = 'No Comment Heading'

                try:
                    comtag = commentbox.find('div', {'class': 'ZmyHeo'})
                    if comtag:
                        custComment= comtag.text.strip()

                except Exception as e:
                    print("Exception while extracting comment:", e)
                    custComment = "No Comment"

                reviews.append({
                    "Product": searchString,
                    "Name": name,
                    "Rating": rating,
                    "CommentHead": commentHead,
                    "Comment": custComment
                })

            # Render the review page
            return render(request, 'review.htm', {"reviews": reviews})

        except Exception as e:
            print("The Exception message is:", e)
            print(traceback.format_exc())
            return HttpResponse("Something went wrong", status=500)

    else:
        crev = card.objects.only("id", "name").order_by('-id')[:6]
        return render(request, 'product.html', {"card": crev})


# ----------------------------------------------------------------------------

 
