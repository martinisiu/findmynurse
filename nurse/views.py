from django.shortcuts import render, get_object_or_404
from .models import Nurse
# Create your views here.

def detail(request, nurse_id):
    nurse = get_object_or_404(Nurse, pk=nurse_id)
    return render(request, 'nurse/more-info.html', {'nurse': nurse})