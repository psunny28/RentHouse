from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import RegistrationForm, UserForm, ProfileForm
from .models import User, Profile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from listings.models import Listing

#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
import requests


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name      = form.cleaned_data['first_name']
            last_name       = form.cleaned_data['last_name']
            phone_number    = form.cleaned_data['phone_number']
            email           = form.cleaned_data['email']
            password        = form.cleaned_data['password']


            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            user.phone_number = phone_number
            user.save()

            #create user profile
            profile =   Profile()
            profile.user_id =   user.id
            profile.profile_picture =   'default/default-user.svg'
            profile.save()

            # account verification
            current_site    =   get_current_site(request)
            mail_subject    =   'Verify Your Account'
            message =   render_to_string('accounts/account_verification_email.html',{
                'user': user,
                'domain': current_site,
                'uid':  urlsafe_base64_encode(force_bytes(user.pk)),
                'token':    default_token_generator.make_token(user),
            })
            to_email    =   email
            send_email  = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(request, 'Thank you for register with us. We have sent a verification email to you, Please check and verify your account. 😀 ')
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistrationForm

    context =   {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email   =   request.POST['email']
        password   =   request.POST['password']

        user    =   auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                # next=/cart/checkout/
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    return redirect('index')

def activate(request, uidb64, token):
    try:
        uid =   urlsafe_base64_decode(uidb64).decode()
        user    =   User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user    =   None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active  =   True
        user.save()
        messages.success(request, 'Congratulations! You have verified your account. You can log in now.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('login')

def forgetpassword(request):
    if request.method == 'POST':
        email   =   request.POST['email']
        if User.objects.filter(email=email).exists():
            user    =   User.objects.get(email__iexact=email)

            # Reset Password email
            current_site    =   get_current_site(request)
            mail_subject    =   'Reset Your Password'
            message =   render_to_string('accounts/reset_password_email.html',{
                'user': user,
                'domain': current_site,
                'uid':  urlsafe_base64_encode(force_bytes(user.pk)),
                'token':    default_token_generator.make_token(user),
            })
            to_email    =   email
            send_email  = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, "Password reset email has been sent to your email address")
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgetpassword')

    return render(request, 'accounts/forgetpassword.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid =   urlsafe_base64_decode(uidb64).decode()
        user    =   User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user    =   None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid']  =   uid
        messages.success(request, 'Please reset your password')
        return redirect('ResetPassword')

def ResetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid =   request.session.get('uid')
            user    =   User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, "Your password has been changed successfully.")
            return redirect('login')
        else:
            messages.error(request, 'Password did not match')
            return redirect('ResetPassword')
    else:
        return render(request, 'accounts/ResetPassword.html')

@login_required(login_url='login')
def dashboard(request):
    userprofile =   get_object_or_404(Profile, user=request.user)
    # my_listing  =   Listing.objects.order_by('-list_date').filter(is_published=True, owner_phone=request.user.phone_number)
    # my_listing_count    =   my_listing.count()

    context =   {
        'userprofile': userprofile,
        # 'my_listing_count': my_listing_count,
    }
    return render(request, 'accounts/dashboard.html', context)

#edit profile
@login_required(login_url='login')
def my_profile(request):
    userprofile =   get_object_or_404(Profile, user=request.user)
    if request.method=='POST':
        user_form   =   UserForm(request.POST, instance=request.user)
        profile_form   =   ProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile has been updated.')
            return redirect('my_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form    =   ProfileForm(instance=userprofile)
    context =   {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/my_profile.html', context)

@login_required(login_url='login')
def my_property(request):
    userprofile =   get_object_or_404(Profile, user=request.user)
    my_listing  =   Listing.objects.order_by('-list_date').filter(is_published=True, owner_phone__iexact=request.user.phone_number, owner_email__exact=request.user.email)
    my_listing_count    =   my_listing.count()

    context =   {
        'userprofile': userprofile,
        'my_listing': my_listing,
        'my_listing_count': my_listing_count,
    }
    return render(request, 'accounts/my_property.html', context)

@login_required(login_url='login')
def change_password(request):
    userprofile =   get_object_or_404(Profile, user=request.user)
    if request.method=='POST':
        current_password    =   request.POST['current_password']
        new_password    =   request.POST['new_password']
        confirm_password    =   request.POST['confirm_password']
        user    =   User.objects.get(email__exact=request.user.email)
        if new_password == confirm_password:
            success =   user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password Changed Successfully.')
                return redirect('change_password')
            else:
                messages.error(request, 'Current password does not match!')
                return redirect('change_password')
        else:
            messages.error(request, 'New pasword did not matched!')
            return redirect('change_password')
    context =   {
        'userprofile': userprofile,
    }
    return render(request, 'accounts/change-password.html', context)

@login_required(login_url='login')
def bookmark_properties(request):
    userprofile =   get_object_or_404(Profile, user=request.user)
    favourites  =   Listing.objects.filter(favourites=request.user)

    context =   {
        'userprofile': userprofile,
        'favourites': favourites,
    }
    return render(request, 'accounts/bookmark-listings.html', context)
