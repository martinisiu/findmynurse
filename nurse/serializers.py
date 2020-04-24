from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Nurse

class NurseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nurse
        fields = ['firstName', 'postCode', 'email']