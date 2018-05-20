# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import anketa.models


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0002_auto_20180505_1658'),
    ]

    operations = [        
        migrations.RemoveField(
            model_name='privilegies',
            name='privdocnomer',
        ),
        migrations.RemoveField(
            model_name='privilegies',
            name='privdocseria',
        ),
        migrations.AlterField(
            model_name='address',
            name='building',
            field=models.CharField(blank=True, verbose_name='Корпус', max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='flat',
            field=models.CharField(blank=True, verbose_name='Квартира', max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='house',
            field=models.CharField(verbose_name='Дом', max_length=5),
            preserve_default=True,
        ),
    ]
