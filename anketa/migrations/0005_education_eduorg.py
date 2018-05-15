# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0004_education_graduationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='eduOrg',
            field=models.ForeignKey(to='anketa.EduOrg', default='', verbose_name='Образовательное учреждение'),
            preserve_default=False,
        ),
    ]
