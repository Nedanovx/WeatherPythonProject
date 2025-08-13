from os import error
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from . import utils

TEMPLATE_DIR = ('os.path.join(BASE_DIR, "templates"),')
def index(request):
    cities = utils.get_five_cities()
    stats = utils.get_stats(cities)
    return render(request, "index.html", {"cities": cities, "stats": stats})

def search_city_view(request):
    city = request.GET.get("city", "").strip()
    if not city:
        return redirect("index")

    city_data = utils.search_city(city)
    if city_data:
        return render(request, "city.html", {"city": city_data})
    else:
        return redirect(f"{reverse('city_not_found')}?error={error}&city={city}")

def city_not_found(request):
    error_message = request.GET.get("error", "Unknown error")
    city_name = request.GET.get("city", "")
    return render(request, "error.html", {
        "error": error_message,
        "city": city_name
    })