# Generated by Django 2.1.7 on 2023-08-25 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230824_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 24, 22, 7, 11, 559740)),
        ),
    ]
