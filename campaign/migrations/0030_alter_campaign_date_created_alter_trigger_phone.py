# Generated by Django 4.1.1 on 2022-10-07 07:53

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Client", "0007_rename_tags_tag"),
        ("campaign", "0029_alter_campaign_date_created_alter_trigger_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 7, 13, 23, 6, 356609)
            ),
        ),
        migrations.AlterField(
            model_name="trigger",
            name="phone",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Client.clientphone",
            ),
            preserve_default=False,
        ),
    ]
