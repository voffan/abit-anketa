# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img',
            old_name='img_content',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='emplcontacts',
            name='contact_type',
            field=models.ForeignKey(verbose_name='Тип контакта', to='anketa.AttrValue'),
        ),
        migrations.AlterField(
            model_name='news',
            name='NewsText',
            field=models.TextField(verbose_name='Контент'),
        ),
    ]
