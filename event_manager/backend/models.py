from django.db import models


class Organization(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(blank=True, upload_to="images/")
    date = models.DateField()
