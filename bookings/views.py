from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def book_now(request):
    return render(request, 'bookings/book_now.html')


@login_required
def payments(request):
    return render(request, 'bookings/payment.html')


@login_required
def booking_confirmed(request):
    return render(request, 'bookings/booking_confirmed.html')
