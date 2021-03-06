# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0004_auto_20161113_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='uid',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, to='tweeter.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, upload_to='/profile_pic/'),
        ),
    ]
