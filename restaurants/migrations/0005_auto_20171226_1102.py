# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20171225_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='categories',
            new_name='category',
        ),
    ]
