# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatemodels', '0018_auto_20160420_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputdata',
            name='download_instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
