from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('search/', views.search_city_view, name="search_city_view"),
               path('error/', views.city_not_found, name="city_not_found"),]