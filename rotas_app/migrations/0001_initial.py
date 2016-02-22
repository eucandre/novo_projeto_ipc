# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 18:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipc_novo_app', '0002_auto_20160222_1044'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomeDoEstabeleciemento', models.CharField(max_length=150)),
                ('Bairro', models.CharField(max_length=150)),
                ('Rua', models.CharField(max_length=150)),
                ('TeleFone', models.CharField(blank=True, max_length=150)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'estabalecimento',
                'verbose_name_plural': 'Estabelecimento',
            },
        ),
        migrations.CreateModel(
            name='rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vizita', models.DateField()),
                ('Item_pesquisado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipc_novo_app.item')),
                ('Local_vizitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotas_app.estabelecimento')),
                ('Pesquisador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfis.perfil')),
                ('SubGrupoParaPesquisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipc_novo_app.subgrupo')),
                ('grupo_para_pesquisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipc_novo_app.pesos_grupos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Rota da pesquisa',
            },
        ),
    ]