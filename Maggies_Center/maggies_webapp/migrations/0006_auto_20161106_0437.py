# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maggies_webapp', '0005_auto_20161106_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempvisitnamemapping',
            name='isInBuilding',
            field=models.BooleanField(default=True),
        ),
    ]