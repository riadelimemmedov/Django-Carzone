# Generated by Django 3.0.7 on 2022-01-24 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20220124_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 24, 9, 38, 1, 840056)),
        ),
    ]
