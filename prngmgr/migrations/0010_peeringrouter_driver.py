# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-10 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prngmgr', '0009_auto_20170410_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='peeringrouter',
            name='driver',
            field=models.CharField(default=b'ios', max_length=10),
        ),
    ]
