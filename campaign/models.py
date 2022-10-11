from datetime import datetime
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db import models

from Client.models import Tag, ClientEvents, ClientPhone, Time


# Create your models here.


class Campaign(models.Model):
    SENT_DAYS_CHOICES = (
        ('Mon', 'Mon'),
        ('Tues', 'Tues'),
        ('Wens', 'Wens'),
        ('Thurs', 'Thurs'),
        ('Fri', 'Fri'),
        ('Sat', 'Sat'),
        ('Sun', 'Sun'),
    )
    # =======================================
    # BASIC CAMPAIGN FIELDS
    # =======================================
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now())
    steps = models.IntegerField(null=True, blank=True)
    in_progress = models.IntegerField(null=True, blank=True)
    complete = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    # =======================================
    # CAMPAIGN SETTINGS FIELDS
    # =======================================
    sending_window = models.BooleanField(null=True, blank=True)
    sent_days = MultiSelectField(choices=SENT_DAYS_CHOICES, max_length=100, null=True, blank=True)
    start_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="start_time")
    end_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="end_time")
    send_number = models.ForeignKey(ClientPhone, on_delete=models.CASCADE, null=True, blank=True)
    double_optin = models.BooleanField(null=True, blank=True, default=False)
    double_optin_keyword = models.CharField(max_length=150, null=True, blank=True)
    double_optin_message = models.TextField(null=True, blank=True)
    limit_multiple = models.BooleanField(null=True, blank=True, default=False)
    limit_multiple_message = models.TextField(null=True, blank=True)
    cancellation_trigger = models.BooleanField(null=True, blank=True, default=False)
    on_reply = models.BooleanField(default=False)

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
    phone = models.ForeignKey(ClientPhone, on_delete=models.CASCADE, null=True, blank=True)
    keyword = models.CharField(max_length=150, null=True, blank=True)
    select_date = models.ForeignKey(ClientEvents, on_delete=models.CASCADE, null=True, blank=True)
    select_before_date = models.CharField(max_length=2, null=True, blank=True, choices=DAYS_CHOICES)
    select_tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)


class Action(models.Model):
    DURATION_CHOICES = (
        ("minutes", "minutes"),
        ("hours", "hours"),
        ("days", "days")
    )
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    text_message = models.TextField(max_length=300, null=True, blank=True)
    number = models.CharField(null=True, blank=True,max_length=50)
    duration = models.CharField(choices=DURATION_CHOICES, null=True, blank=True, max_length=50)
    wait_until = models.TimeField(null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
