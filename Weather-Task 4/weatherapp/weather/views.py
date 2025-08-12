from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import utils

TEMPLATE_DIR = ('os.path.join(BASE_DIR, "templates"),')
def index(request):
    cities = utils.get_five_cities()
    stats = utils.get_stats(cities)
    return render(request, "index.html", {"cities": cities, "stats": stats})

def search_city_view(request):
    city = request.GET.get("city", "").strip()
    if not city:
        return render(request, "error.html")

    city_data = utils.search_city(city)
    if city_data:
        return render(request, "city.html", {"city": city_data})
    else:
        return redirect("city_not_found")

def city_not_found(request):
    return render(request, "error.html")