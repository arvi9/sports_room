# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 17:02
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import equipment.utility


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=equipment.utility.get_due_date)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('TTR', 'TT Racket'), ('SHR', 'Shuttle Racket')], max_length=3)),
                ('n_equipment', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment')),
            ],
            options={
                'ordering': ['book_date'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13)),
                ('fine', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=7)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='queue',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Student'),
        ),
        migrations.AddField(
            model_name='borroweditem',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment'),
        ),
        migrations.AddField(
            model_name='borroweditem',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Student'),
        ),
    ]
