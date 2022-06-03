from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from listings.models import Listing
from agents.models import Agent
from listings.choices import bedroom_choices, bathroom_choices, price_choices, city_choices, availability_choices, property_choices
from content.models import banner, aboutus, TeamMember

def index(request):

    listings    =   Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    agents  =   Agent.objects.order_by('-hire_date').filter(is_mvp=True)[:4]
    flistings    =   Listing.objects.order_by('-list_date').filter(is_published=True, is_it_featured_property=True)[:8]

    AgraListings    =   Listing.objects.filter(city__icontains="agra").count()
    DelhiListings    =   Listing.objects.filter(Q(city__icontains='delhi') |Q(city__icontains='new delhi')).count()
    GurgaonListings    =   Listing.objects.filter(Q(city__icontains='gurgaon') |Q(city__icontains='gurugram')).count()
    BangaloreListings    =   Listing.objects.filter(Q(city__icontains='bangalore') |Q(city__icontains='bangaluru') |Q(city__icontains='bengalore')).count()
    PatnaListings    =   Listing.objects.filter(Q(city__icontains='patna') |Q(city__icontains='bihar')).count()
    MumbaiListings    =   Listing.objects.filter(Q(city__icontains='mumbai') |Q(city__icontains='bombey') |Q(city__icontains='bumbai')).count()

    context =   {
        'AgraListings'          :        AgraListings,
        'DelhiListings'         :       DelhiListings,
        'GurgaonListings'       :     GurgaonListings,
        'BangaloreListings'     :   BangaloreListings,
        'PatnaListings'         :       PatnaListings,
        'MumbaiListings'        :      MumbaiListings,
        'listings'              :           listings,
        'agents'                :           agents,
        'flistings'             :           flistings,
        'bedroom_choices'       :    bedroom_choices,
        'bathroom_choices'      :    bathroom_choices,
        'price_choices'         :   price_choices,
        'city_choices'          :   city_choices,
        'availability_choices'  :   availability_choices,
        'property_choices'      :   property_choices,
    }
    return render(request, 'index.html', context)

def agra_city(request):
    listings    =   Listing.objects.order_by('-list_date').filter(city__icontains='agra')
    paginator   =   Paginator(listings, 25)
    page    =   request.GET.get('page')
    paged_listings  =   paginator.get_page(page)
    listing_count   =   listings.count()


    context =   {
        'listings': listings,
        'listing_count':    listing_count,
    }
    return render(request, 'listings/cities/agralistings.html', context)

def delhi_city(request):
    listings    =   Listing.objects.order_by('-list_date').filter(Q(city__icontains='delhi') |Q(city__icontains='new delhi'))
    paginator   =   Paginator(listings, 25)
    page    =   request.GET.get('page')
    paged_listings  =   paginator.get_page(page)
    listing_count   =   listings.count()


    context =   {
        'listings': listings,
        'listing_count':    listing_count,
    }
    return render(request, 'listings/cities/delhilistings.html', context)

def gurgaon_city(request):
    listings    =   Listing.objects.order_by('-list_date').filter(Q(city__icontains='gurgaon') |Q(city__icontains='gurugram'))
    paginator   =   Paginator(listings, 25)
    page    =   request.GET.get('page')
    paged_listings  =   paginator.get_page(page)
    listing_count   =   listings.count()


    context =   {
        'listings': listings,
        'listing_count':    listing_count,
    }
    return render(request, 'listings/cities/gurgaonlistings.html', context)

def bangalore_city(request):
    listings    =   Listing.objects.order_by('-list_date').filter(Q(city__icontains='bangalore') |Q(city__icontains='bangaluru') |Q(city__icontains='bengalore'))
    paginator   =   Paginator(listings, 25)
    page    =   request.GET.get('page')
    paged_listings  =   paginator.get_page(page)
    listing_count   =   listings.count()


    context =   {
        'listings': listings,
        'listing_count':    listing_count,
    }
    return render(request, 'listings/cities/bangalorelistings.html', context)

def patna_city(request):
    listings    =   Listing.objects.order_by('-list_date').filter(Q(city__icontains='patna') |Q(city__icontains='bihar'))
    paginator   =   Paginator(listings, 25)
    page    =   request.GET.get('page')
    paged_listings  =   paginator.get_page(page)
    listing_count   =   listings.count()


    context =   {
        'listings': listings,
        'listing_count':    listing_count,
    }
    return render(request, 'listings/cities/patnalistings.html', context)

def mumbai_city(request):
    listings    =   Listing.objects.order_by('-list_date').filter(Q(city__icontains='mumbai') |Q(city__icontains='bombey') |Q(city__icontains='bumbai'))
    paginator   =   Paginator(listings, 25)
    page    =   request.GET.get('page')
    paged_listings  =   paginator.get_page(page)
    listing_count   =   listings.count()


    context =   {
        'listings': listings,
        'listing_count':    listing_count,
    }
    return render(request, 'listings/cities/mumbailistings.html', context)

def about_us(request):
    aboutcontent =   aboutus.objects.all()
    AboutTeamMembers   =   TeamMember.objects.all()


    context =   {
        'aboutcontent': aboutcontent,
        'AboutTeamMembers' :   AboutTeamMembers,
    }
    return render(request, 'pages/about_us.html', context)

def membership_plans(request):
    return render(request, 'membership/membership_plans.html')
