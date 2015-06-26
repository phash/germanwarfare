# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_auto_20150625_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fahrzeug',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='waffe',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
