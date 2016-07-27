# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatemodels', '0032_remove_impactmodel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterglobal',
            name='calibration',
            field=models.NullBooleanField(default=None, verbose_name='Was the model calibrated?'),
        ),
        migrations.AlterField(
            model_name='waterglobal',
            name='vegetation',
            field=models.NullBooleanField(default=None, verbose_name='Is CO2 fertilisation accounted for?'),
        ),
        migrations.AlterField(
            model_name='waterregional',
            name='calibration',
            field=models.NullBooleanField(default=None, verbose_name='Was the model calibrated?'),
        ),
        migrations.AlterField(
            model_name='waterregional',
            name='vegetation',
            field=models.NullBooleanField(default=None, verbose_name='Is CO2 fertilisation accounted for?'),
        ),
    ]