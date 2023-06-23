# Generated by Django 4.2.2 on 2023-06-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_patient_age_patient_district_patient_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='consultation_time',
            new_name='consultation_time_end',
        ),
        migrations.AddField(
            model_name='doctor',
            name='consultation_time_start',
            field=models.TimeField(null=True),
        ),
    ]
