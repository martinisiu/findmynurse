from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from nurse.models import Nurse
# Create your views here.

class HomePageView(TemplateView):
    template_name = "search/index.html"

class SearchResultsView(ListView):
    model = Nurse
    template_name = 'search/search-results.html'

    


    def get_queryset(self): # new
        q = self.request.GET.get('q')
        #Turns the postcode to an area ie. SE17xb returns Lambeth
        lat,lng, area = Nurse.getAreaData(self, q)
        object_list = Nurse.objects.filter(
            Q(primary_care_trust__icontains=area)
        )

        return object_list
        
class Test(TemplateView):
    template_name = "search/test.html"

class About(TemplateView):
    template_name = "search/about.html"