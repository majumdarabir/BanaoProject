from django.contrib import admin
from .models import DoctorModel
from .models import PatientModel
# Register your models here.
admin.site.register(DoctorModel)
admin.site.register(PatientModel)