# Generated by Django 4.1.1 on 2022-10-07 09:41

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaign", "0036_alter_campaign_date_created_alter_campaign_sent_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 7, 15, 11, 29, 724712)
            ),
        ),
    ]
