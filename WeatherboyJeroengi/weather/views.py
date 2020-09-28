from django.shortcuts import render
from .models import Page
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.paginator import Paginator
import threading

# Create your views here.

# Since I did not get the refresh-functionality working on the ListView-page, 
# I made this separate refreshing-page.
def refresh(request):
    from weather.retrieve_new_entry import main
    main()
    context = {
        'entries': Page.objects.all(),
    }
    return render(request, 'weather/index.html', context=context)
    
# This class, that is an extension of ListView, handles the
# adding of new data to the database.
class EntryList(ListView):
    paginate_by = 10
    template_name = 'weather/index.html'
    context_object_name = 'entries' # Name for referencing all the Page objects in the HTML template
    ordering = ['-date'] # We want to order the data from greatest (== most recent) to smallest
    model = Page # This retrieves all objects matching Page from the database. A similar SQL query would be:
    """
    SELECT temperature, date
    FROM Page
    ORDER BY date DESC
    """
        