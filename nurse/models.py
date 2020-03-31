from django.db import models
import json
import requests

# Create your models here.
class Nurse(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100) 
    fullName = str(firstName) + " " + str(lastName)
    postCode = models.CharField(max_length=10)
    area = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.firstName
    
    def getArea(self, postcode):
        areaFile = requests.get('http://api.postcodes.io/postcodes/SE17XB')
        data = areaFile.json()
        for d in data['results']:
            print(p['primary_care_trust'])

    