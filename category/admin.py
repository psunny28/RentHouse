from django.contrib import admin
from .models import Category, State, City

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields =   {'slug': ('name',)}
    list_display    =   ('name', 'slug')

admin.site.register(Category, CategoryAdmin)
# class StateAdmin(admin.ModelAdmin):
admin.site.register(State)

class CityAdmin(admin.ModelAdmin):
    list_display    =   ('name', 'state',)
admin.site.register(City, CityAdmin)
