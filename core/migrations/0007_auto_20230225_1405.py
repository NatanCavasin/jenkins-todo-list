# Generated by Django 2.1.7 on 2023-02-25 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230225_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 25, 14, 5, 5, 161471)),
        ),
    ]
