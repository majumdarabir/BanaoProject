# Generated by Django 4.1 on 2023-02-27 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_doctor_patient_delete_doctor_model_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctor',
            new_name='DoctorModel',
        ),
        migrations.RenameModel(
            old_name='Patient',
            new_name='PatientModel',
        ),
    ]