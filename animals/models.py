from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

ANIMAL_CHOICES = (
    ('Cat', 'CAT'),
    ('Dog', 'DOG'),
    ('Bird', 'BIRD'),
    ('Reptile', 'REPTILE'),
)

AGE_CHOICES = (
    ('Young', 'YOUNG'),
    ('Old', 'OLD'),
)

GENDER_CHOICES = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
)


class Animal(models.Model):
    name = models.CharField(max_length=28, null=False, blank=False)
    image = models.ImageField(upload_to='media/', default=None)
    description = models.TextField(max_length=400, default=None)
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=None
    )
    animal = models.CharField(choices=ANIMAL_CHOICES, max_length=7, default=None)
    age = models.CharField(choices=AGE_CHOICES, max_length=5, default=None)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default=None)
    sheltered = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
