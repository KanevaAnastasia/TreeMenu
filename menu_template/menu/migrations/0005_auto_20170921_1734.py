# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20170921_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='parent_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Item', verbose_name='id Родителя'),
        ),
    ]
