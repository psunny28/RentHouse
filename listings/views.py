from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing, PropertyGallary
from .choices import bedroom_choices, bathroom_choices, price_choices, city_choices, availability_choices, property_choices
from .forms import Add_Listing
from agents.models import Agent
from accounts.models import User, Profile
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


# Create your views here.
def listings(request):
    listings    =   Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator   =   Paginator(listings, 25)
    page    =   request.GET.get('page')
    paged_listings  =   paginator.get_page(page)
    listing_count   =   listings.count()

    context =   {
        'listings': paged_listings,
        'listing_count':    listing_count,
        'bedroom_choices'  :   bedroom_choices,
        'bathroom_choices' :   bathroom_choices,
        'price_choices'     :   price_choices,
        'city_choices'      :   city_choices,
        'availability_choices'  :   availability_choices,
        'property_choices'     :   property_choices,
        'values': request.GET
    }
    return render(request, 'listings/listings.html', context)

def listing(request, ListingSlug, id, category_slug):
    listing =   get_object_or_404(Listing, slug=ListingSlug, pk=id, property_type__slug=category_slug)
    is_favourites = False
    if listing.favourites.filter(id=request.user.id).exists():
        is_favourites = True

    listing.views   =   listing.views + 1
    listing.save()

    #get property gallery images
    property_gallery    =   PropertyGallary.objects.filter(property_id=listing.id)

    context =   {
        'listing':  listing,
        'property_gallery': property_gallery,
        'is_favourites': is_favourites,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list   =   Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords    =   request.GET['keywords']
        if keywords:
            queryset_list   =   queryset_list.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords) | Q(address__icontains=keywords) | Q(pincode__icontains=keywords) | Q(slug__icontains=keywords)| Q(city__icontains=keywords))
    if 'bedroom' in request.GET:
        bedroom    =   request.GET['bedroom']
        if bedroom:
            queryset_list   =   queryset_list.filter(bedroom__iexact=bedroom)
    if 'bathroom' in request.GET:
        bathroom    =   request.GET['bathroom']
        if bathroom:
            queryset_list   =   queryset_list.filter(bathroom__lte=bathroom)
    if 'price' in request.GET:
        price    =   request.GET['price']
        if price:
            queryset_list   =   queryset_list.filter(price__lte=price)
    if 'city' in request.GET:
        city    =   request.GET['city']
        if city:
            queryset_list   =   queryset_list.filter(city__iexact=city)
    if 'available_for' in request.GET:
        available_for    =   request.GET['available_for']
        if available_for:
            queryset_list   =   queryset_list.filter(available_for__icontains=available_for)
    if 'property_type' in request.GET:
        property_type    =   request.GET['property_type']
        if property_type:
            queryset_list   =   queryset_list.filter(property_type__name__icontains=property_type)
    if 'AirConditioning' in request.GET:
        AirConditioning    =   request.GET['AirConditioning']
        if AirConditioning:
            queryset_list   =   queryset_list.filter(ameneties__icontains=AirConditioning)
    listing_count   =   queryset_list.count()

    context =   {
        'listings': queryset_list,
        'listing_count': listing_count,
        'bedroom_choices'  :   bedroom_choices,
        'bathroom_choices' :   bathroom_choices,
        'price_choices'     :   price_choices,
        'city_choices'      :   city_choices,
        'availability_choices'  :   availability_choices,
        'property_choices'     :   property_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

def featured_listings(request):
    featured_listings    =   Listing.objects.order_by('list_date').filter(is_published=True, is_it_featured_property=True)
    listing_count   =   featured_listings.count()

    context =   {
        'listings': featured_listings,
        'listing_count': listing_count,
        'bedroom_choices'  :   bedroom_choices,
        'bathroom_choices' :   bathroom_choices,
        'price_choices'     :   price_choices,
        'city_choices'      :   city_choices,
        'availability_choices'  :   availability_choices,
        'property_choices'     :   property_choices,
        'values': request.GET
    }
    return render(request, 'listings/featured_listings.html', context)

@login_required(login_url='login')
def add_listing(request):
    context =   {}
    form    =   Add_Listing()
    if request.method=="POST":
        form    =   Add_Listing(request.POST, request.FILES)
        if form.is_valid():
            data    =   form.save(commit=False)
            data.slug = slugify(data.title)
            login_user  =   Agent.objects.get(email=request.user.id)
            data.agent    =   login_user
            data.save()
            messages.success(request, 'Property has been been submitted successfully. It will be verified soon!')
    context['form'] =   form
    return render (request, 'listings/add_listing.html', context)

@login_required
def add_favourite(request, id):
    listing =   get_object_or_404(Listing, pk=id)
    if listing.favourites.filter(id=request.user.id).exists():
        messages.warning(request, "Property succussfully removed from favourites!!!")
        listing.favourites.remove(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        listing.favourites.add(request.user)
        messages.success(request, 'Property succussfully added in your favourite list.')
        return HttpResponseRedirect(listing.get_absolute_url())
