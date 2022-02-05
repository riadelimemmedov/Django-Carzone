# Generated by Django 3.0.7 on 2022-01-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('designation', models.CharField(max_length=255, verbose_name='Designation')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('facebook_link', models.URLField(max_length=255, verbose_name='Facebook')),
                ('twitter', models.URLField(max_length=255, verbose_name='Twitter')),
                ('goggle_plus_link', models.URLField(max_length=255, verbose_name='GogglePlus')),
            ],
        ),
    ]
