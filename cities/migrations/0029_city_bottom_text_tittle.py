# Generated by Django 4.1.7 on 2023-06-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0028_cityimage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='bottom_text_tittle',
            field=models.CharField(default=1, max_length=100, verbose_name='bottom_text_tittle'),
            preserve_default=False,
        ),
    ]
