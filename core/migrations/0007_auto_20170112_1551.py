# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_price_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='menuitem',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
