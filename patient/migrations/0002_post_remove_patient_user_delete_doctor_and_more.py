# Generated by Django 4.1 on 2023-02-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]