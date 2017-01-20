# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatemodels', '0068_auto_20170120_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impactmodel',
            name='responsible_person',
            field=models.CharField(blank=True, help_text='Contact information for person responsible for model simulations in this simulation round, if not the model contact person', max_length=500, null=True, verbose_name='Person responsible for model simulations in this simulation round'),
        ),
    ]
