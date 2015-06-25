# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0004_auto_20150625_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Munition',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=200)),
                ('schaden', models.IntegerField()),
                ('durchschlag', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='waffe',
            name='durchschlag',
        ),
        migrations.RemoveField(
            model_name='waffe',
            name='schaden',
        ),
        migrations.AddField(
            model_name='waffe',
            name='munitionen',
            field=models.ManyToManyField(to='compare.Munition'),
        ),
    ]
