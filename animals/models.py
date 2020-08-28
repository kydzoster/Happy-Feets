from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=28, null=False, blank=False)
