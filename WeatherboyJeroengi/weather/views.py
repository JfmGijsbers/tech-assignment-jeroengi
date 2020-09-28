from django.shortcuts import render
from .models import Page
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    #temperature_list = Page.objects.all()
    #paginator = Paginator(temperature_list, 10)

    #page_number = request.GET('page')
    #page_obj = paginator.get_page(page_number)
    # context = {}
    if request.method == 'POST' and 'run_script' in request.POST:
        # Import the script that refreshes entries
        from weather.retrieve_new_entry import main

        main()
        
        return HttpResponseRedirect('')
        #return render(request, 'weather/index.html', context=context)

    context = {
        'entries': Page.objects.all(),
        #'page_obj': page_obj
    }
    return render(request, 'weather/index.html', context=context) #context = context

    
class EntryList(ListView):
    #from weather.retrieve_new_entry import main
    #main()
    paginate_by = 10
    template_name = 'weather/index.html'
    context_object_name = 'entries'
    ordering = ['-date']
    model = Page
        