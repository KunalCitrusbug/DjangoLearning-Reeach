# Generated by Django 4.1.1 on 2022-10-11 10:04

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Client", "0009_alter_clientevents_date_alter_clientevents_name_and_more"),
        ("campaign", "0042_alter_campaign_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 11, 15, 34, 59, 389902)
            ),
        ),
        migrations.AlterField(
            model_name="trigger",
            name="phone",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Client.clientphone",
            ),
        ),
    ]
