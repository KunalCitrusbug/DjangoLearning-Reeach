# Generated by Django 4.1.1 on 2022-10-11 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0041_rename_actions_action_alter_campaign_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 15, 31, 42, 144099)),
        ),
    ]
