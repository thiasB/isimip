# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-03 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climatemodels', '0080_auto_20170424_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseimpactmodel',
            name='owners',
        ),
    ]
