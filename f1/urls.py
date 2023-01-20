from django.urls import path
from . import views

app_name = 'f1'

urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/', views.drivers, name='drivers'),
    path('constructors/', views.constructors, name='constructors'),
    path('circuits/', views.circuits, name='circuits'),
    path('races/', views.races, name='races'),
    path('races/<int:round>/qualifyings/',
         views.qualifyings, name='qualifyings'),
    path('races/<int:round>/race_results/',
         views.race_results, name='race_results'),
    path('races/<int:round>/pit_stops/', views.pit_stops, name='pit_stops'),
    path('races/<int:round>/lap_times/', views.lap_times, name='lap_times'),
    path('races/<int:round>/driver_standings/',
         views.driver_standings, name='driver_standings'),
    path('races/<int:round>/constructor_standings/', views.constructor_standings,
         name='constructor_standings'),
]
