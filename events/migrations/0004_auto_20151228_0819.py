# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151228_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.URLField(default=None),
        ),
    ]
