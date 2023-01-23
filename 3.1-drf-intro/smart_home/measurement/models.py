from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.CharField(max_length=30, required=False, verbose_name='Описание')
