# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fahrzeug',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=200)),
                ('tier', models.IntegerField(default=1, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')])),
                ('ruhm', models.IntegerField()),
                ('kosten', models.IntegerField()),
                ('besatzung', models.IntegerField()),
                ('turmdrehen', models.IntegerField()),
                ('hitpoints', models.IntegerField()),
                ('topgeschwindigkeit', models.FloatField()),
                ('beschleunigung', models.FloatField()),
                ('sichtweite', models.IntegerField()),
                ('wanneFront', models.IntegerField()),
                ('wanneSeite', models.IntegerField()),
                ('wanneHeck', models.IntegerField()),
                ('turmFront', models.IntegerField()),
                ('turmSeite', models.IntegerField()),
                ('turmHeck', models.IntegerField()),
                ('art', models.ForeignKey(to='compare.Art')),
            ],
        ),
        migrations.CreateModel(
            name='Waffe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=200)),
                ('dpm', models.IntegerField()),
                ('aimtime', models.FloatField()),
                ('reloadtime', models.FloatField()),
                ('durchschlag', models.IntegerField()),
                ('munition', models.IntegerField()),
                ('schaden', models.IntegerField()),
                ('genauigkeit', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='fahrzeug',
            name='waffen',
            field=models.ManyToManyField(to='compare.Waffe'),
        ),
    ]
