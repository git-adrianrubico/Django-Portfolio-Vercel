# Generated by Django 5.0.7 on 2024-07-15 20:19

import apps.portfolio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.portfolio.models.Portfolio.get_upload_to),
        ),
    ]
