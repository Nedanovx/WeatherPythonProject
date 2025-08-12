from django.shortcuts import render
from django.http import HttpResponse
from . import utils

TEMPLATE_DIR = ('os.path.join(BASE_DIR, "templates"),')
def index(request):
    cities = utils.get_five_cities()
    stats = utils.get_stats(cities)
    return render(request, "index.html", {"cities": cities, "stats": stats})
