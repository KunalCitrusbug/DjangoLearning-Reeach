# Generated by Django 4.1.1 on 2022-10-07 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0027_alter_campaign_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 13, 21, 31, 980086)),
        ),
    ]