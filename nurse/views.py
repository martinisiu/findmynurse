from django.shortcuts import render, get_object_or_404
from .models import Nurse

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NurseSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
# Create your views here.

def detail(request, nurse_id):
    nurse = get_object_or_404(Nurse, pk=nurse_id)
    return render(request, 'nurse/more-info.html', {'nurse': nurse})

class NurseList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        nurses = Nurse.objects.all()
        serializer = NurseSerializer(nurses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        nurse = NurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostCodeToNurse(APIView):
    renderer_classes = [JSONRenderer]

    def get_nurse(self, postcode):
        try:
            return Nurse.objects.get(primary_care_trust=Nurse.getAreaData(self, postcode)[2])
        except Nurse.DoesNotExist:
            raise Http404
    
    def get(self, request, postcode, format=None):
        nurse = self.get_nurse(postcode)
        serializer = NurseSerializer(nurse)
        return Response(serializer.data)
