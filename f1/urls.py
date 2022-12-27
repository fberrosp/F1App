from django.urls import path
from . import views

app_name = 'f1'

urlpatterns = [
    path('', views.index, name='index'),
    path('circuits/', views.circuits, name='circuits'),
    path('constructors/', views.constructors, name='constructors'),
    path('drivers/', views.drivers, name='drivers'),
    path('seasons/', views.seasons, name='seasons')
]