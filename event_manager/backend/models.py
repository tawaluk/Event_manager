from django.db import models


class Organization(models.Model):
    """Модель организации."""

    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Event(models.Model):
    """Модель ивента."""

    title = models.CharField(max_length=100)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    date = models.DateField()