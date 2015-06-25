# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0006_munition_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='munition',
            old_name='schaden',
            new_name='schadenmax',
        ),
        migrations.AddField(
            model_name='munition',
            name='schadenmin',
            field=models.IntegerField(default=datetime.datetime(2015, 6, 25, 21, 27, 46, 914991, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
