from django.db import models

# Create your models here.
class card(models.Model):
    pname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    subject = models.CharField(max_length=80)
    desc =  models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.pname

################################################################################## 