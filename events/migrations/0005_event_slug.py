# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20151228_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
    ]
