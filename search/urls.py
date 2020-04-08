from django.urls import path,include

from . import views 

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('about/', views.About.as_view(), name='about'),
   path('search/', views.SearchResultsView.as_view(), name='search_results')
]
