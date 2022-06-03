from django.urls import path
from .import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('appointment', views.appointment, name='appointment'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('submit-property-request/', views.property_request, name='property_request'),
]
