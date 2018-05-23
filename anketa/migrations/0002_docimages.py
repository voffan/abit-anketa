# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import anketa.models


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocImages',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to=anketa.models.DocImagePath)),
                ('doc', models.ForeignKey(verbose_name='Документ', to='anketa.Docs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
