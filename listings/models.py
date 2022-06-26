from django.db import models
from multiselectfield import MultiSelectField
# from location_field.models.plain import PlainLocationField
from datetime import datetime
from agents.models import Agent
from PIL import Image, ImageDraw, ImageFont
from category.models import Category
from accounts.models import User
from django.core.validators import RegexValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeCanvas, ResizeToFill, ResizeToFit
from django.urls import reverse

class Watermark(object):
    def process(self, img):
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', 30)
        text = '© RENTHOUSE.CO.IN'
        draw.text((650, 700), text, fill=(242, 243, 244, 1), font = font)
        return img

class Listing(models.Model):
    agent   =   models.ForeignKey(
        Agent,
        models.SET_NULL,
        null=True,
    )
    property_type   =   models.ForeignKey(Category, on_delete=models.CASCADE)
    availability_allowed   =   (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Couples', 'Couples'),
        ('Unisex', 'Unisex'),
        ('Family', 'Family'),
        ('Student', 'Student'),
        ('All', 'All')
    )
    available_for   =   MultiSelectField(choices=availability_allowed, max_choices=3)
    title   =   models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, unique=False)
    floor   =   models.CharField(max_length=20)
    description   =   models.TextField(blank=False)
    address   =   models.CharField(max_length=100)
    state   =   models.CharField(max_length=30)
    city   =   models.CharField(max_length=30)
    pincode   =   models.CharField(max_length=6)
    # landmark   =   models.CharField(max_length=100, blank=True)
    # location = PlainLocationField(based_fields=['landmark'], zoom=13, blank=True)
    location = models.CharField(max_length=800, null=True, help_text ="(Please enter latitude and longitude of this property/location). Example: 28.4930741,77.0946958")
    price   =   models.IntegerField()
    bedroom   =   models.IntegerField()
    bathroom   =   models.IntegerField()
    area_sqft_size   =   models.IntegerField()
    property_age   =   models.CharField(max_length=20)
    kitchen_type    =   (
        ('Not Available', 'Not Available'),
        ('Normal Kitchen', 'Normal Kitchen'),
        ('Modular Kitchen', 'Modular Kitchen')
    )
    kitchen =   models.CharField(max_length=100, blank=True, default='Modular Kitchen', choices=kitchen_type)
    parking_type = (
        ('Free Parking', 'Free Parking'),
        ('Paid Parking', 'Paid Parking'),
    )
    parking = models.CharField(max_length=50, blank=False, default='Free Parking', choices=parking_type)
    furniture_type = (
        ('Unfurnished', 'Unfurnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Fully-Furnished', 'Fully-Furnished'),
    )
    furnished_type = models.CharField(max_length=50, blank=False, default='Unfurnished', choices=furniture_type)
    security_amount = models.CharField(max_length=100, blank=False)
    sharing_type = (
        ('Allowed', 'Allowed'),
        ('Not Allowed', 'Not Allowed'),
    )
    sharing = models.CharField(max_length=50, blank=False, default='Allowed', choices=sharing_type)
    internet_facility = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )
    internet = models.CharField(max_length=50, blank=False, default='Available', choices=internet_facility)
    ameneties_list   =   (
        ('Air Conditioning', 'AirConditioning'),
        ('Swimming Pool', 'SwimmingPool'),
        ('Elevator', 'Elevator'),
        ('Laundry Room', 'LaundryRoom'),
        ('Window Covering', 'WindowCovering'),
        ('Pets Allowed', 'PetsAllowed'),
        ('Free WIFI', 'FreeWIFI'),
        ('Gyser', 'Gyser'),
        ('Refrigerator', 'Refrigerator'),
        ('TV', 'TV'),
        ('GYM', 'GYM'),
        ('Car Parking', 'CarParking'),
        ('Alarm', 'Alarm'),
        ('Power backup', 'Powerbackup'),
        ('Park', 'Park'),
        ('RO Water', 'ROWater'),
        ('CCTV Camera', 'CCTVCamera'),


    )
    ameneties   =   MultiSelectField(blank=False, choices=ameneties_list)
    owner_name  =   models.CharField(max_length=100)
    owner_email =   models.EmailField(max_length=100)
    owner_phone =   models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10, blank=False)
    owner_secondary_phone =   models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=10, blank=True,help_text ="(Optional)")
    owner_photo =   ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(400, 400)],format='JPEG', options={'quality': 80}, blank=False)
    photo_main = ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark(), Watermark()],format='JPEG', options={'quality': 70}, blank=False)
    front_home_photo = ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark()],format='JPEG', options={'quality': 70}, blank=False)
    first_room_photo = ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark()],format='JPEG', options={'quality': 70}, blank=False)
    second_room_photo = ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark()],format='JPEG', options={'quality': 70}, blank=True, help_text ="(Optional)")
    third_room_photo = ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark()],format='JPEG', options={'quality': 70}, blank=True, help_text ="(Optional)")
    kitchen_photo = ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark()],format='JPEG', options={'quality': 70}, blank=True, help_text ="(Optional)")
    bathroom_photo = ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark()],format='JPEG', options={'quality': 70}, blank=False)
    property_video = models.FileField(upload_to='videos/property_videos/%Y/%m/%d/', default=None, blank=True, help_text ="(Optional)")
    views   =   models.IntegerField(default=0, editable=False)
    favourites  =   models.ManyToManyField(User, related_name='favorite', default=None, blank=True, editable=False)
    no_of_days_advance=models.IntegerField(default=0, editable=False)
    start_date=models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, editable=False)
    is_published = models.BooleanField(default=False)
    is_it_featured_property = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name    =   'listing'
        verbose_name_plural =   'Properties'

    def get_absolute_url(self):
        return reverse('listing', args=[self.id, self.property_type.slug, self.slug])

    def __str__(self):
        return self.title


class PropertyGallary(models.Model):
    property = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image  =   ProcessedImageField(upload_to='images/property_images/%Y/%m/%d/', processors=[ResizeToFill(1600, 1080), Watermark()],format='JPEG', options={'quality': 70}, max_length=200)

    def __str__(self):
        return self.property.title
    class Meta:
        verbose_name    =   'propertygallary'
        verbose_name_plural =   'Property Gallery'
