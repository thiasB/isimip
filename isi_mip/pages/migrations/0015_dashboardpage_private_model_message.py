# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_impactmodelspage_private_model_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardpage',
            name='private_model_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
