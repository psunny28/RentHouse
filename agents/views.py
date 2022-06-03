from django.shortcuts import render, get_object_or_404
from .models import Agent
from listings.models import Listing

# Create your views here.
def agents(request):
    agents  =   Agent.objects.all()

    context =   {
        'agents': agents,
    }
    return render(request, 'agents/agents.html', context)

def single_agent(request, agent_id):
    agent   = get_object_or_404(Agent, pk=agent_id)
    listings   =   Listing.objects.order_by('-list_date').filter(is_published=True, agent=agent_id)[:10]
    agent_listing_count =   listings.count()
    featured_listings    =   Listing.objects.order_by('list_date').filter(is_published=True, is_it_featured_property=True)[:10]


    context =   {
        'agent': agent,
        'listings': listings,
        'agent_listing_count': agent_listing_count,
        'featured_listings':    featured_listings,
    }
    return render(request, 'agents/single_agent.html', context)
