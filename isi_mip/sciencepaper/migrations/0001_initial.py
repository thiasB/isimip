# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('homepage', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('doi', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('journal_name', models.CharField(blank=True, max_length=500, null=True)),
                ('journal_volume', models.IntegerField(blank=True, null=True)),
                ('journal_number', models.IntegerField(blank=True, null=True)),
                ('journal_pages', models.CharField(blank=True, max_length=500, null=True)),
                ('first_published', models.DateField(blank=True, null=True)),
                ('authors', models.ManyToManyField(blank=True, to='sciencepaper.Author')),
            ],
        ),
    ]
