from django.contrib import admin
from django.urls import path
from . import views
from .views import EntryList


from weather.retrieve_new_entry import main
main()

urlpatterns = [
    path('', EntryList.as_view(), name='weather-home'),
    path('refresh/', views.refresh, name='refresh')
]
