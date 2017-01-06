# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsRoomConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='equipment',
            name='category',
            field=models.CharField(choices=[('TTR', 'TT Racket'), ('TTB', 'TT Ball'), ('SHR', 'Shuttle Racket'), ('SHC', 'Shuttlecock'), ('FTB', 'Football'), ('CBL', 'Cricket Ball'), ('CBT', 'Cricket Bat')], max_length=3),
        ),
    ]
