# Generated by Django 4.1.1 on 2022-10-06 12:18

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaign", "0011_alter_campaign_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 6, 17, 48, 52, 591635)
            ),
        ),
    ]
