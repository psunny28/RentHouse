from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Contact, ContactUs, Appointment, PropertyRequest
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id  =   request.POST['listing_id']
        listing  =   request.POST['listing']
        name  =   request.POST['name']
        city  =   request.POST['city']
        pincode  =   request.POST['pincode']
        email  =   request.POST['email']
        phone  =   request.POST['phone']
        message  =   request.POST['message']
        user_id  =   request.POST['user_id']
        agent_email  =   request.POST['agent_email']

         #  Check if user has made inquiry already
        # if request.user.is_authenticated:
        #   user_id = request.user.id
        #   has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        #   if has_contacted:
        #     messages.error(request, 'You have already made an inquiry for this listing, Please wait our agent will contact you asap. We are sorry for the inconvenience.')
        #     return redirect('/listings/'+listing_slug)

        contact =   Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id, city=city, pincode=pincode)

        contact.save()
        # send mail
        send_mail(
            'Property Inquiry for ' + listing,
            message + '\n\n There has been an inquiry for ' + listing + '\n Please sign in for more info.\n\n Regards\n Rent House',
            'renthouse.co.in@gmail.com',
            [agent_email,  'harimohansharma1999@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for making an inquiry! We have received your request and our agents will get back to you as soon as possible!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

def appointment(request):
    if request.method == 'POST':
        listing_id  =   request.POST['listing_id']
        listing  =   request.POST['listing']
        name  =   request.POST['name']
        city  =   request.POST['city']
        pincode  =   request.POST['pincode']
        email  =   request.POST['email']
        phone  =   request.POST['phone']
        appointment_date  =   request.POST['appointment_date']
        message  =   request.POST['message']
        user_id  =   request.POST['user_id']
        agent_email  =   request.POST['agent_email']
        owner_email  =   request.POST['owner_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
          user_id = request.user.id
          has_contacted = Appointment.objects.all().filter(listing_id=listing_id, user_id=user_id)
          if has_contacted:
            messages.error(request, 'You have already made an inquiry for this listing, Please wait our agent will contact you asap. We are sorry for the inconvenience.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        appointment =   Appointment(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, appointment_date=appointment_date, message=message, user_id=user_id, city=city, pincode=pincode)

        appointment.save()
        # send mail
        send_mail(
            'Property Inquiry for ' + listing,
            message + '\n\nThere has been an inquiry for ' + listing + '\nCustomer Name = ' + name + '\ncontact number = ' + phone +'\n\nRegards\nRent House',
            'renthouse.co.in@gmail.com',
            [agent_email, owner_email,  'sabhay381@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for making an appointment! We have received your request and owner or agents will get back to you as soon as possible!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

def contact_us(request):
    if request.method   ==  'POST':
        name   =   request.POST['name']
        email   =   request.POST['email']
        phone_number   =   request.POST['phone_number']
        subject =   request.POST['subject']
        message    =   request.POST['message']
        attachment    =   request.POST['attachment']

        contact = ContactUs(name=name, email=email, phone_number=phone_number, subject=subject, message=message, attachment=attachment)
        contact.save()

        #send mail
        # send_mail(
        #     subject,
        #     message,
        #     email,
        #     ['harimohansharma1999@gmail.com'],
        #     fail_silently=False,
        # )

        messages.success(request, 'Thank you '+ name +' for contacting us. We have received your inquiry and our agent will contact you as soon as possible.')
        return redirect('contact_us')
    return render(request, 'pages/contact_us.html')

def property_request(request):
    if request.method=="POST":
        property_title  =   request.POST['property_title']
        avail_for  =   request.POST['avail_for']
        property_type  =   request.POST['property_type']
        price  =   request.POST['price']
        bedroom  =   request.POST['bedroom']
        bathroom  =   request.POST['bathroom']
        address  =   request.POST['address']
        address  =   request.POST['address']
        city  =   request.POST['city']
        state  =   request.POST['state']
        pincode  =   request.POST['pincode']
        name  =   request.POST['name']
        email  =   request.POST['email']
        phone  =   request.POST['phone']
        secondary_phone  =   request.POST['secondary_phone']

        submit_proeprty_request =   PropertyRequest(property_title=property_type, avail_for=avail_for, property_type=property_type, price=price, bedroom=bedroom, bathroom=bathroom,
                                                    address=address, city=city, state=state, pincode=pincode, name=name, email=email, phone=phone, secondary_phone=secondary_phone)
        submit_proeprty_request.save()
        messages.success(request, "Your request has been submitted successfully, Our executive or agent will contact you as soon as possible. Thank You!")

    return render(request, 'listings/property_request.html')
