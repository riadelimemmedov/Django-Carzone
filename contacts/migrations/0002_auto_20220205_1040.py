# Generated by Django 3.0.7 on 2022-02-05 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='create_date_message_notification',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 5, 10, 40, 31, 61714)),
        ),
    ]