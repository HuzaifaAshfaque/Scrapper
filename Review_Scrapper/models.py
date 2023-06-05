from django.db import models

# Create your models here.
class card(models.Model):
    ppic = models.ImageField(upload_to='static/pimages/',default="")
    pname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=int)
    rating = models.IntegerField()
    subject = models.CharField(max_length=80)
    desc =  models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.pname

################################################################################## 

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    desc =models.TextField()
    date = models.DateField()
    def __str__(self) :
        return self.name
    

####################################################################################

class Search(models.Model):
    s_query= models.CharField(max_length=30)
    def __str__(self) :
        return self.s_query
    

####################################################################################