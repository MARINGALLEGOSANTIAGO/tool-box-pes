# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PES_APP', '0004_auto_20170504_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('Pei', 'Pereira'), ('Ddas', 'Dosquebradas')], default='Pei', max_length=15, verbose_name='Ciudad'),
        ),
    ]
