# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20160519_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='button_name',
            field=models.CharField(default='Submit', max_length=500, verbose_name='Button name'),
        ),
    ]
