# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatemodels', '0040_set_simulation_round_20170112_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationround',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]