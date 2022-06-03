from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    listing =   models.CharField(max_length=200)
    listing_id  =   models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=False)
    contact_date    =   models.DateTimeField(default=datetime.now, blank=True)
    user_id =   models.IntegerField(blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name    =   'contact'
        verbose_name_plural =   'property inquiries'

class ContactUs(models.Model):
    name    =   models.CharField(max_length=100)
    email   =   models.EmailField(max_length=50)
    phone_number    =   models.CharField(max_length=15)
    subject =   models.CharField(max_length=200)
    message =   models.TextField(blank=False)
    contact_date    =   models.DateTimeField(default=datetime.now, blank=True)
    attachment = models.FileField(upload_to='contact_us/attachments/%Y/%m/%d/', default=None, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name    =   'contactus'
        verbose_name_plural =   'contact us'

class Appointment(models.Model):
    listing =   models.CharField(max_length=200)
    listing_id  =   models.IntegerField()
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    appointment_date    =   models.DateTimeField(null=True)
    message = models.TextField(blank=False)
    contact_date    =   models.DateTimeField(default=datetime.now, blank=True)
    user_id =   models.IntegerField(blank=True)

    def __str___(self):
        return self.name

class PropertyRequest(models.Model):
    property_title   =   models.CharField(max_length=250, blank=False)
    property_type   =   models.CharField(max_length=250, blank=False)
    avail_for   =   models.CharField(max_length=250, blank=False)
    price   =   models.IntegerField(blank=False)
    bedroom   =   models.IntegerField(blank=False)
    bathroom   =   models.IntegerField(blank=False)
    description =   models.TextField(blank=True)
    address   =   models.CharField(max_length=100, blank=False)
    state   =   models.CharField(max_length=30, blank=False)
    city   =   models.CharField(max_length=30, blank=False)
    pincode   =   models.CharField(max_length=6, blank=False)
    name    =   models.CharField(max_length=100, blank=False)
    email   =   models.EmailField(max_length=100, blank=False)
    phone =   models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=11, blank=False)
    secondary_phone =   models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=11, blank=True,help_text ="(Optional)")
    contact_date    =   models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name    =   'PropertyRequest'
        verbose_name_plural =   'Propety Post Requests'

    def __str__(self):
        return self.property_title
