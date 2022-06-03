from django.db import models
from listings.models import Listing
from accounts.models import User
from datetime import datetime

# Create your models here.

class Payment(models.Model):
    user        =   models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id  =   models.CharField(max_length=100)
    payment_method  =   models.CharField(max_length=100)
    amount_paid =   models.CharField(max_length=100) #total amound paid by the customer
    status  =   models.CharField(max_length=100)
    created_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

class Booking(models.Model):
    property_id    =   models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_id        =   models.ForeignKey(User, on_delete=models.CASCADE)
    checkin        =   models.DateField(auto_now=False, auto_now_add=False)
    checkout       =   models.DateField(auto_now=False, auto_now_add=False, blank=True)
    adults         =   models.IntegerField()
    kids           =   models.IntegerField(default=0)
    price          =   models.FloatField()
    booked_on      =   models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Booking ID: "+str(self.id)

    @property
    def is_past_due(self):
        return date.today()>self.checkout
