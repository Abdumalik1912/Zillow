from django.shortcuts import render, get_object_or_404
from listings.models import Home
from .forms import HomeSearchForm

# Create your views here.


def search_home(request):
    homes = Home.objects.all()
    form = HomeSearchForm(request.GET)
    if form.is_valid():
        city = form.cleaned_data.get('city')
        owner = form.cleaned_data.get('owner')
        price = form.cleaned_data.get('price')

        if city:
            homes = homes.filter(city__icontains=city)
        if owner:
            homes = homes.filter(owner__icontains=owner)
        if price:
            homes = homes.filter(price__lte=price)
    context = {
        'homes': homes,
        'form': form
    }

    return render(request, 'search_home.html', context)
