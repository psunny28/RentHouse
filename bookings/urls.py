from django.urls import path
from .import views

urlpatterns = [
    path('book_now/', views.book_now, name='book_now'),
    path('payments/', views.payments, name='payments'),
    path('payments/bookingconfirmed/', views.booking_confirmed, name='booking_confirmed'),
]
