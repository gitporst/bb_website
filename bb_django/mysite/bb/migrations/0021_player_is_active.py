# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bb', '0020_remove_player_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
