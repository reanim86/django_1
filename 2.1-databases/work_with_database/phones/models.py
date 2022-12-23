from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=20)



