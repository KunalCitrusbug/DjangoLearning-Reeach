# Generated by Django 4.1.1 on 2022-10-16 11:10

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaign", "0049_alter_campaign_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 16, 16, 40, 22, 267629)
            ),
        ),
    ]
