# Generated by Django 4.1.1 on 2022-10-06 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Client', '0003_rename_anniversary_clientevents_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientevents',
            name='date',
        ),
        migrations.RemoveField(
            model_name='clientevents',
            name='name',
        ),
        migrations.AddField(
            model_name='clientevents',
            name='anniversary',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clientevents',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientphone',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
