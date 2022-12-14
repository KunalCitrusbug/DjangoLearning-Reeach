# Generated by Django 4.1.1 on 2022-10-06 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Client", "0002_alter_clientevents_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clientevents",
            old_name="anniversary",
            new_name="date",
        ),
        migrations.RemoveField(
            model_name="clientevents",
            name="birthdate",
        ),
        migrations.AddField(
            model_name="clientevents",
            name="name",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="clientevents",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
