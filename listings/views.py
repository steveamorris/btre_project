from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .choices import price_choices, bedroom_choices, state_choices


from .models import Listing

# Create your views here.

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  page_listings = paginator.get_page(page)

  context = {
    'listings': page_listings
  }
  return render(request, 'listings/listings.html', context)




def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  context3 = {
    'listing': listing
  }
  return render(request, 'listings/listing.html', context3)

def search(request):
  context4 = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices
  }
  return render(request, 'listings/search.html', context4)

