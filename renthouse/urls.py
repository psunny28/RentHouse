from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_title = 'RENTHOUSE ADMIN'
admin.site.index_title  =   'Rent House Administration'

urlpatterns = [
    path("", views.index, name='index'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('renthouse-secure-adminlogin/', admin.site.urls),
    path('listings/', include('listings.urls')),
    path('agents/', include('agents.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('bookings/', include('bookings.urls')),
    path('faq/', include('faq.urls')),
    path("about-us/", views.about_us, name='about_us'),
    path("membership-plans/", views.membership_plans, name='membership_plans'),
    path("agra-city-listings/", views.agra_city, name='agra_city'),
    path("delhi-city-listings/", views.delhi_city, name='delhi_city'),
    path("gurgaon-city-listings/", views.gurgaon_city, name='gurgaon_city'),
    path("bangalore-city-listings/", views.bangalore_city, name='bangalore_city'),
    path("patna-city-listings/", views.patna_city, name='patna_city'),
    path("mumbai-city-listings/", views.mumbai_city, name='mumbai_city'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
