# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20170924_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(max_length=200, verbose_name='URL'),
        ),
    ]
