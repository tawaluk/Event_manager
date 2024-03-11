from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from backend.models import Organization


class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(editable=True)
    REQUIRED_FIELDS = ('username',)
    USERNAME_FIELD = 'email'
    organizations = models.ManyToManyField(Organization, blank=True)

    def __str__(self):
        return self.email
