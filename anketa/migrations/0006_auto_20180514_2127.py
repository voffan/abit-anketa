# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0005_education_eduorg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='docIssuer',
            field=models.ForeignKey(to='anketa.AttrValue', related_name='DocIssuer', blank=True, verbose_name='Орган выдавший документ', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docs',
            name='docType',
            field=models.ForeignKey(to='anketa.AttrValue', related_name='DocType_docs', blank=True, verbose_name='Тип документа', null=True),
            preserve_default=True,
        ),
    ]
