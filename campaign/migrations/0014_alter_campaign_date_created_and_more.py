# Generated by Django 4.1.1 on 2022-10-06 12:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0007_rename_tags_tag'),
        ('campaign', '0013_alter_campaign_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 18, 10, 13, 84028)),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='select_tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.tag'),
        ),
    ]