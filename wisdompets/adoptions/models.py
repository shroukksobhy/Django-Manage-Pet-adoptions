from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=30, blank=True)
    submitter = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    description = models.TextField()
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    submission_date = models.DateTimeField()
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
