# Generated by Django 4.1.1 on 2022-10-17 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0053_alter_campaign_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 9, 50, 49, 876628)),
        ),
    ]
