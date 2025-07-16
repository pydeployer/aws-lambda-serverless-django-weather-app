from django.db import models


class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']
        db_table = 'cities'

    def __str__(self):
        return f"{self.name}, {self.country}"
