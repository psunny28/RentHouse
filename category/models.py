from django.db import models
# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name    =   'City'
        verbose_name_plural =   'Cities'

    def __str__(self):
        return self.name

class Category(models.Model):
    name    =   models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name    =   'category'
        verbose_name_plural =   'property categories'



    def __str__(self):
        return self.name
