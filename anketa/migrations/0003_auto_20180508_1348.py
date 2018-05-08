# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0002_docimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='serialno',
            field=models.BigIntegerField(blank=True, verbose_name='Серия документа', db_index=True, max_length=15, null=True),
            preserve_default=True,
        ),
    ]
