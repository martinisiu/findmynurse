from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from nurse.models import Nurse
# Create your views here.

class HomePageView(TemplateView):
    template_name = "search/homepage.html"

class SearchResultsView(ListView):
    model = Nurse
    template_name = 'search/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Nurse.objects.filter(
            Q(firstName__icontains=query) | Q(lastName__icontains=query) | Q(area__icontains=query)
        )
        return object_list
        
class Test(TemplateView):
    template_name = "search/test.html"

class About(TemplateView):
    template_name = "search/about.html"