# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maggies_webapp', '0006_auto_20161106_0437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tempvisitnamemapping',
            old_name='isInBuilding',
            new_name='is_in_Building',
        ),
        migrations.AddField(
            model_name='tempvisitnamemapping',
            name='centre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maggies_webapp.Centre'),
            preserve_default=False,
        ),
    ]