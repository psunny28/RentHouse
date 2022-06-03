from django.contrib import admin
from .models import Booking, Payment
import admin_thumbnails

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'property_id', 'user_id', 'checkin', 'checkout', 'booked_on',)
    list_display_links  =   ('id', 'property_id', 'user_id', 'checkin', 'checkout', 'booked_on',)
    list_per_page   =   25

class PaymentAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'user', 'amount_paid', 'status', 'created_at')
    list_display_links  =   ('id', 'user', 'amount_paid',)
    list_per_page   =   25

admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)
