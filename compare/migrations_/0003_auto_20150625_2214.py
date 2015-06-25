# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_auto_20150625_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 6, 25, 20, 14, 27, 410687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fahrzeug',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 6, 25, 20, 14, 27, 411687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='waffe',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 6, 25, 20, 14, 27, 409679, tzinfo=utc)),
        ),
    ]
