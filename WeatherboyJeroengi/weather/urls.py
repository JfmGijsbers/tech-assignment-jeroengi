from django.contrib import admin
from django.urls import path
from . import views
from .views import EntryList

urlpatterns = [
    path('', views.home, name='weather-home'),
    path('history/', EntryList.as_view(), name='weather-history')
]
