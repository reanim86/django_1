# Generated by Django 4.1.5 on 2023-01-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_sensor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]
