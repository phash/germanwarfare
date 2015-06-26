# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0005_auto_20150625_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='munition',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 21, 19, 44, 29193, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
