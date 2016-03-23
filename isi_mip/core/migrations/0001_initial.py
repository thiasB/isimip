# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('_name', models.CharField(blank=True, help_text="If left empty, the target's title will be used.", max_length=255, null=True, verbose_name='Alt. name')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FooterLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeaderLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('_name', models.CharField(blank=True, help_text="If left empty, the target's title will be used.", max_length=255, null=True, verbose_name='Alt. name')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeaderLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='headerlink',
            name='header',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='header_links', to='core.HeaderLinks'),
        ),
        migrations.AddField(
            model_name='headerlink',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='footerlink',
            name='footer',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_links', to='core.FooterLinks'),
        ),
        migrations.AddField(
            model_name='footerlink',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page'),
        ),
    ]
