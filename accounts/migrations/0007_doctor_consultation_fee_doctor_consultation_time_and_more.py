# Generated by Django 4.2.2 on 2023-06-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_doctor_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='consultation_fee',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='consultation_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.CharField(choices=[('national', 'National Hospital'), ('evercare', 'Evercare Hospital'), ('islami', 'Islami Bank Hospital'), ('memon', 'Memon Maternity Hospital'), ('ctg-edical', 'Chittagong Medical College Hospital'), ('square', 'Square Hospital'), ('popular', 'Popular Diagnostic Centre Ltd'), ('labaid', 'Labaid Hospitals'), ('ibn-ina', 'Ibn Sina Specialized Hospital')], default='national', max_length=30),
        ),
        migrations.AddField(
            model_name='doctor',
            name='location',
            field=models.CharField(choices=[('ctg', 'Chittagong'), ('dhaka', 'Dhaka')], default='dhaka', max_length=20),
        ),
    ]
