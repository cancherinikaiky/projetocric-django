# Generated by Django 4.1.7 on 2023-09-21 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0034_rename_enrollmentfields_enrollmentfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='enrollment_fields',
        ),
        migrations.DeleteModel(
            name='EnrollmentField',
        ),
    ]
