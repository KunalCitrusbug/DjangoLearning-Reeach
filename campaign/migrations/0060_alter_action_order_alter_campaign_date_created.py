# Generated by Django 4.1.1 on 2022-10-17 07:33

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaign", "0059_alter_action_order_alter_campaign_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="order",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 17, 13, 3, 24, 460465)
            ),
        ),
    ]
