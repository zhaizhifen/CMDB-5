# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20170705_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='slot',
            field=models.CharField(max_length=64, verbose_name='插槽位'),
        ),
    ]
