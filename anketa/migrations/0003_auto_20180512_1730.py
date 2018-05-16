# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import anketa.models


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0002_auto_20180505_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to=anketa.models.DocImagePath)),
                ('doc', models.ForeignKey(verbose_name='Документ', to='anketa.Docs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
