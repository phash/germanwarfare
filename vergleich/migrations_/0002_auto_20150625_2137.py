# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 19, 37, 14, 612439, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fahrzeug',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 19, 37, 23, 20270, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waffe',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 19, 37, 28, 388326, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
