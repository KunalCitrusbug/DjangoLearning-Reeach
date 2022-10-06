from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from Client.models import Tag


# Create your models here.


class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now())
    steps = models.IntegerField(null=True, blank=True)
    in_progress = models.IntegerField(null=True, blank=True)
    complete = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class Trigger(models.Model):
    DAYS_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    type = models.TextField(max_length=300)
    phone = models.CharField(max_length=12)
    keyword = models.CharField(max_length=150,null=True, blank=True)
    select_date = models.DateField(null=True, blank=True)
    select_before_date = models.CharField(max_length=2, null=True, blank=True,choices=DAYS_CHOICES)
    select_tags = models.ForeignKey(Tag, on_delete=models.CASCADE,null=True, blank=True)