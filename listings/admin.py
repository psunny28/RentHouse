from django.contrib import admin
from .models import Listing, PropertyGallary
import admin_thumbnails
from agents.models import Agent
from .forms import Add_Listing
from accounts.models import User

@admin_thumbnails.thumbnail('image')
class PropertyGallaryInline(admin.TabularInline):
    model = PropertyGallary
    extra = 1

@admin_thumbnails.thumbnail('photo_main',)
class ListingAdmin(admin.ModelAdmin):
    prepopulated_fields =   {'slug': ('title',)}
    list_display    =   ('id', 'title', 'property_type', 'city', 'price', 'list_date', 'agent', 'is_published',)
    list_display_links  =   ('title',)
    list_filter =   ('list_date', 'is_published', 'city', 'agent', 'property_type')
    # list_editable   =   ('is_published',)
    search_fields   =   ('title', 'description', 'city', 'state', 'pincode', 'price')
    inlines =   [PropertyGallaryInline]
    list_per_page   =   25
    # ordering = ('id',)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "agent":
    #         kwargs["queryset"] = Agent.objects.filter(email=request.user.id)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
            if request.user.is_admin or request.user.is_superuser:
                self.exclude = ()
            else:
                self.exclude = ('is_published', 'start_date',)
            return super(ListingAdmin, self).get_form(request, obj=None, **kwargs)


admin.site.register(Listing, ListingAdmin)
admin.site.register(PropertyGallary)
