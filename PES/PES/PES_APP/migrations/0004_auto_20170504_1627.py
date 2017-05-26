# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PES_APP', '0003_auto_20170504_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_user',
            name='city',
            field=models.CharField(choices=[('Pei', 'Pereira'), ('Ddas', 'Dosquebradas')], default='Pei', max_length=15, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='profile_user',
            name='payment',
            field=models.CharField(choices=[('Efe', 'Efectivo'), ('Tcred', 'Tarjeta de cr\xe9dito o d\xe9bito')], default='Efe', max_length=15, verbose_name='Pago'),
        ),
    ]