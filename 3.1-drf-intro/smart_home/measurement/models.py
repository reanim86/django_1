from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, verbose_name='Фото')

