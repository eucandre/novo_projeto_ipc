# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rotas_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estabelecimento',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='rota',
            name='usuario',
        ),
        migrations.AlterModelTable(
            name='estabelecimento',
            table=None,
        ),
    ]
