# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='NewsText',
            field=models.CharField(verbose_name='Контент', max_length=700),
        ),
    ]
