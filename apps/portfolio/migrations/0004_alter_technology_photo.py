# Generated by Django 4.2.6 on 2023-11-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_technology_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
