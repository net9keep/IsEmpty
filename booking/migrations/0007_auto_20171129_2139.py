# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20171129_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
