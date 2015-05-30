# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import staff.models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20150528_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(help_text='150x150px', verbose_name='Имя', upload_to=staff.models.imagepath),
        ),
    ]
