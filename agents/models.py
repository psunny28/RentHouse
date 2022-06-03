from django.db import models
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from accounts.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeCanvas, ResizeToFill


# Create your models here.
class Department(models.Model):
    name    =   models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Supervisor(models.Model):
    email    =   models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True, 'is_active':True},)
    Employee_ID =   models.CharField(max_length=8, blank=False)
    Department  =   models.ForeignKey(Department, on_delete=models.CASCADE, blank=True)
    designation    =   models.CharField(max_length=100, blank=True)
    city    =   models.CharField(max_length=100, blank=True)
    phone   =   models.CharField(max_length=13)
    photo   =   ProcessedImageField(upload_to='images/supervisors/%Y/%m/%d/', processors=[ResizeToFill(400, 400)],format='JPEG', options={'quality': 80}, blank=False)
    is_mvp  =   models.BooleanField(default=False)
    hire_date   =   models.DateTimeField(default=datetime.now, blank=True)


    def name(self):
        return f'{self.email.first_name} {self.email.last_name}'

    def __str__(self):
        return f'{self.email.first_name} {self.email.last_name}'

class Agent(models.Model):
    supervisor_name =   models.ForeignKey(Supervisor, models.SET_NULL, null=True,)
    email   =   models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_realtor': True, 'is_active':True},)
    Department  =   models.ForeignKey(Department, on_delete=models.CASCADE, blank=True)
    Employee_ID =   models.CharField(max_length=8)
    photo   =   ProcessedImageField(upload_to='images/agents/%Y/%m/%d/', processors=[ResizeToFill(400, 400)],format='JPEG', options={'quality': 80}, blank=False)
    designation    =   models.CharField(max_length=100)
    city    =   models.CharField(max_length=100)
    description    =   models.TextField(blank=True)
    phone   =   models.CharField(max_length=13)
    is_mvp  =   models.BooleanField(default=False)
    hire_date   =   models.DateTimeField(default=datetime.now, blank=True)

    def name(self):
        return f'{self.email.first_name} {self.email.last_name}'

    def __str__(self):
        return f'{self.email.first_name} ({self.Employee_ID})'
