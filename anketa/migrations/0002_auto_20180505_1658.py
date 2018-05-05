# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='privilegies',
            name='privdocnomer',
            field=models.IntegerField(default=0, verbose_name='Номер документа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privilegies',
            name='privdocseria',
            field=models.IntegerField(default=0, verbose_name='Серия документа'),
            preserve_default=False,
        ),
    ]
