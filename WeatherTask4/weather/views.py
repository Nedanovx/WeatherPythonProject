from django.shortcuts import render
from django.http import HttpResponse

TEMPLATES_DIR = (
    'os.path.join(BASE_DIR, "templates"),'
)
def index(request):
    return render(request, 'index.html'"")

