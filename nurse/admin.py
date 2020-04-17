from django.contrib import admin

from .models import Nurse, PDFFile
# Register your models here.
admin.site.register(Nurse)
admin.site.register(PDFFile)