from django.db import models
import json
import requests

# Create your models here.

class Nurse(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    fullName = str(firstName) + " " + str(lastName)
    postCode = models.CharField(max_length=10, default="")
    area = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=True)
    lattiude = models.FloatField(max_length=10, null=True)
    longitude = models.FloatField(max_length=10, null=True)

    def __init__(self):
        x = 3141

    def __str__(self):
        return self.firstName

    """
    def getArea(self, postcode):
        areaFile = requests.get('http://api.postcodes.io/postcodes/SE17XB')
        data = areaFile.json()
        for d in data['results']:
            print(p['primary_care_trust'])

    def get(postalcode):
    apiCall = requests.get('http://api.postcodes.io/postcodes/' + postalcode)
    data = apiCall.json()
    latitude = data['result']['latitude']
    longitude = data['result']['longitude']

    return (latitude, longitude)
    """
