from django import forms

class NewNurseForm(forms.Form):
    firstName = forms.CharField(label="First Name", max_length=100)
    lastName = forms.CharField(label="Last Name", max_length=100)
    postcode = forms.CharField(label="Post Code", max_length=10)
    phoneNumber = forms.CharField(label="Phone Number", max_length=20)
    email = forms.EmailField(label="Email", max_length=50)
