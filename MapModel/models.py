from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Loc(models.Model):
    x = models.FloatField(max_length=10)
    y = models.FloatField(max_length=10)
    attribute = models.CharField(max_length=20)
