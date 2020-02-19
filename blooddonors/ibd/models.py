from datetime import datetime

from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Donor(models.Model):
    donor_name = models.CharField(max_length=100,default='', blank=True)
    blood_group_choices = (
        ('A +ve', 'A +ve'),
        ('A -ve', 'A -ve'),
        ('B +ve', 'B +ve'),
        ('B -ve', 'B -ve'),
        ('AB +ve', 'AB +ve'),
        ('AB -ve', 'A -ve'),
        ('A1 +ve', 'A1 +ve'),
        ('A1 -ve', 'A1 -ve'),
        ('A2 +ve', 'A2 +ve'),
        ('A2 -ve', 'A2 -ve'),
        ('A1B +ve', 'A1B +ve'),
        ('A1B -ve"', 'A1B -ve"'),
        ('A2B +ve', 'A2B +ve'),
        ('A2B -ve"', 'A2B -ve"'),
        ('O +ve', 'O +ve'),
        ('O -ve', 'O -ve'),
    )
    blood_group = models.CharField(max_length=10,choices=blood_group_choices,default= " ")
    donor_std  = models.CharField(max_length=3)
    donor_zip  = models.CharField(max_length=6)
    donor_phone = models.CharField(max_length=10)
    donor_email = models.EmailField(unique= True,max_length=254)
    donor_pass = models.CharField(max_length=20)

    def __str__(self):
        return  self.donor_name


class DonorHistory(models.Model):
    req_phone = models.CharField(max_length=10)
    req_reply = models.CharField(max_length=50)
    req_date = models.DateTimeField(default=datetime.now, blank=True)
    donors_hist = models.ForeignKey(Donor,on_delete= models.CASCADE)

    def __str__(self):
        return self.req_phone

    class Meta:
        ordering = ['req_phone']