# Generated by Django 4.1.1 on 2022-10-17 05:48

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Client", "0009_alter_clientevents_date_alter_clientevents_name_and_more"),
        ("campaign", "0054_action_type_alter_campaign_date_created"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="action",
            name="action",
        ),
        migrations.RemoveField(
            model_name="action",
            name="order",
        ),
        migrations.AddField(
            model_name="action",
            name="duration",
            field=models.CharField(
                blank=True,
                choices=[("minutes", "minutes"), ("hours", "hours"), ("days", "days")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="action",
            name="number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="action",
            name="tag",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Client.tag",
            ),
        ),
        migrations.AddField(
            model_name="action",
            name="text_message",
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="action",
            name="wait_until",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 17, 11, 18, 21, 850421)
            ),
        ),
    ]
