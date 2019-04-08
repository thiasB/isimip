# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-08 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climatemodels', '0094_auto_20190404_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='biomes',
            name='compute_soil_carbon',
            field=models.TextField(blank=True, default='', null=True, verbose_name='How do you compute soil organic carbon during land use (do you mix the previous PFT SOC into agricultural SOC)?'),
        ),
        migrations.AddField(
            model_name='biomes',
            name='harvest_npp_crops',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Do you harvest NPP of crops? Do you including grazing? How does harvested NPP decay?'),
        ),
        migrations.AddField(
            model_name='biomes',
            name='npp_litter_output',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Does non-harvested crop NPP go to litter in your output?'),
        ),
        migrations.AddField(
            model_name='biomes',
            name='seperate_soil_carbon',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Do you separate soil organic carbon in pasture from natural grass?'),
        ),
        migrations.AddField(
            model_name='biomes',
            name='simulate_bioenergy',
            field=models.TextField(blank=True, default='', null=True, verbose_name='How do you simulate bioenergy? I.e. What PFT do you simulate on bioenergy land?'),
        ),
        migrations.AddField(
            model_name='biomes',
            name='simulate_pasture',
            field=models.TextField(blank=True, default='', null=True, verbose_name='How do you simulate pasture (which PFT)?'),
        ),
        migrations.AddField(
            model_name='biomes',
            name='transition_cropland',
            field=models.TextField(blank=True, default='', null=True, verbose_name='How do you simulate the transition from cropland to bioenergy?'),
        ),
        migrations.AddField(
            model_name='biomes',
            name='treat_biofuel_npp',
            field=models.TextField(blank=True, default='', null=True, verbose_name='How do you to treat biofuel NPP and biofuel harvest?'),
        ),
    ]
