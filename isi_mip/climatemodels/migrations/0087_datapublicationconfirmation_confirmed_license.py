# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-21 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatemodels', '0086_datapublicationconfirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapublicationconfirmation',
            name='confirmed_license',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
