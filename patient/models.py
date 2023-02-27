from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
# class Patient(models.Model):
#     user =models.OneToOneField(User,on_delete=models.CASCADE)
#     # add other field  
# class Doctor(models.Model):
#     user =models.OneToOneField(User,on_delete=models.CASCADE)
class DoctorModel(models.Model):
    fname =models.TextField()
    lname=models.TextField()
    email=models.EmailField()
    uname=models.TextField()
    pic=models.ImageField(upload_to='profiles')
    def __str__(self):
        return str(self.uname) 
class PatientModel(models.Model):
    fname =models.TextField()
    lname=models.TextField()
    email=models.EmailField()
    uname=models.TextField()
    image=models.ImageField()
    pic=models.ImageField(upload_to='profiles')
    def __str__(self):
        return str(self.uname) 