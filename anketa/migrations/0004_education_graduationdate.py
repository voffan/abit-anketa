# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0003_auto_20180512_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='graduationDate',
            field=models.DateField(default=datetime.datetime(2018, 5, 12, 15, 12, 20, 594514, tzinfo=utc), verbose_name='Дата окончания'),
            preserve_default=False,
        ),
    ]
