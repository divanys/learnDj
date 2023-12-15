from django.db import models


class Prosuct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name