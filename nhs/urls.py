"""nhs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from search import views
from nurse import views as nurseviews

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #API ABove
    #path('nurses/', nurseviews.NurseList.as_view()),
    path('api/<str:postcode>', nurseviews.PostCodeToNurse.as_view()),
    #API
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
    path('nurse/', include('nurse.urls')),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
