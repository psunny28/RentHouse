from django.contrib import admin
from .models import Contact, ContactUs, Appointment, PropertyRequest
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display    =   ('id', 'name',  'email', 'phone', 'listing', 'city', 'pincode', 'message', 'contact_date',)
    list_filter    =   ('city', 'pincode', 'contact_date',)
    list_display_links  =   ('id', 'name', 'listing')
    search_fields   =   ('id', 'name', 'email')
    list_per_page = 50

class ContactUsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display    =   ('id', 'name',  'email', 'phone_number', 'message', 'contact_date',)
    list_display_links  =   ('id', 'name', 'email',)
    search_fields   =   ('id', 'name', 'email')
    list_per_page = 25

class AppointmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display    =   ('id', 'name',  'email', 'phone', 'listing', 'city', 'pincode', 'message', 'contact_date',)
    list_display_links  =   ('id', 'name', 'listing')
    list_filter    =   ('city', 'pincode', 'contact_date',)

class PropertyRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display    =   ('id', 'name', 'phone', 'property_title', 'price', 'city', 'pincode', 'contact_date')
    list_display_links  =   ('id', 'name', 'property_title',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(PropertyRequest, PropertyRequestAdmin)
