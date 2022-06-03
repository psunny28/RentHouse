from django.urls import path
from .import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:id>/<slug:category_slug>/<slug:ListingSlug>', views.listing, name='listing'),
    path('search/', views.search, name='search'),
    path('featured_listings/', views.featured_listings, name='featured_listings'),
    path('add_listing/', views.add_listing, name='add_listing'),
    path('<int:id>/', views.add_favourite, name='add_favourite'),
]
