# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
