from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Client's phone numbers
class ClientPhone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.phone


# Clients special dates
class ClientEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "ClientEvent"


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Time(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
