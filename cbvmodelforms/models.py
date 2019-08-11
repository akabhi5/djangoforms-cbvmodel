from django.db import models
from django.urls import reverse

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('home')
