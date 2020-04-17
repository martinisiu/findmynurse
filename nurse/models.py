from django.db import models
import json
import requests

# Create your models here.

class Nurse(models.Model):
    firstName = models.CharField(max_length=100, default="", verbose_name="First Name")
    lastName = models.CharField(max_length=100,default="", verbose_name="Last Name")
    postCode = models.CharField(max_length=10, default="", verbose_name="Postal code")
    phoneNumber = models.CharField(max_length=20, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, null=True)
    latitude = models.FloatField(max_length=10, default=0)
    longitude = models.FloatField(max_length=10, default=0)
    primary_care_trust = models.CharField(max_length=100, default="N/A")

    def save(self, *args, **kwargs):
        data = self.getAreaData(self.postCode)
        self.latitude = data[0]
        self.longitude = data[1]
        self.primary_care_trust = data[2]
        super().save(self, *args, **kwargs)
        
    def __str__(self):
        return self.firstName + " " + self.lastName

    def getAreaData(self, postcode):
        response = requests.get("https://api.postcodes.io/postcodes/" + str(postcode))
        data = response.json()
        lat = data['result']['latitude']
        longitude = data['result']['longitude']
        primarycaretrust = data['result']['primary_care_trust']
        return (lat, longitude, primarycaretrust)

class PDFFile(models.Model):
    pdffile = models.FileField(null = True, blank=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "File for " + self.nurse.primary_care_trust + " area"
