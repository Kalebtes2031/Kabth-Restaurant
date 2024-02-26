# Generated by Django 5.0.2 on 2024-02-25 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='comment',
        ),
        migrations.AddField(
            model_name='booking',
            name='preferredDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='booking',
            name='preferredTime',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AddField(
            model_name='booking',
            name='specialRequests',
            field=models.TextField(blank=True, null=True),
        ),
    ]