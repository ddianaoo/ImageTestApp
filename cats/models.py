from django.db import models
from images.models import Image


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
