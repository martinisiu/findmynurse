from django.urls import path,include

from . import views

urlpatterns = [
   path('<int:nurse_id>/', views.detail, name='detail'),
]
