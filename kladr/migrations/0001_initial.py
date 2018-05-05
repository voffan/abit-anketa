# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Altnames',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('oldcode', models.CharField(verbose_name='Старый код', max_length=19)),
                ('newcode', models.CharField(verbose_name='Новый код', max_length=19)),
                ('level', models.CharField(verbose_name='Уровень объекта', max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doma',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, verbose_name='Номера домов', max_length=40)),
                ('korp', models.CharField(db_index=True, blank=True, null=True, verbose_name='Корпус дома', max_length=10)),
                ('socr', models.CharField(verbose_name='Сокращенное наименование типа объекта', max_length=10)),
                ('code', models.CharField(db_index=True, verbose_name='Код', max_length=19)),
                ('index', models.CharField(db_index=True, blank=True, null=True, verbose_name='Почтовый индекс', max_length=6)),
                ('gninmb', models.CharField(db_index=True, blank=True, null=True, verbose_name='Код ИФНС', max_length=4)),
                ('uno', models.CharField(db_index=True, blank=True, null=True, verbose_name='Код терр-го участка ИФНС', max_length=4)),
                ('ocatd', models.CharField(db_index=True, blank=True, null=True, verbose_name='ОКАТО', max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, verbose_name='Номер квартиры', max_length=40)),
                ('code', models.CharField(db_index=True, verbose_name='Код', max_length=23)),
                ('index', models.CharField(db_index=True, blank=True, null=True, verbose_name='Почтовый индекс', max_length=6)),
                ('gninmb', models.CharField(blank=True, null=True, verbose_name='Код ИФНС(ИМНС)', max_length=4)),
                ('uno', models.CharField(blank=True, null=True, verbose_name='Код терр-го участка ИФНС', max_length=4)),
                ('np', models.CharField(blank=True, null=True, verbose_name='Номер подъезда', max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kladr',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, verbose_name='Наименование', max_length=40)),
                ('socr', models.CharField(verbose_name='Сокращенное наименование типа объекта', max_length=10)),
                ('code', models.CharField(db_index=True, verbose_name='Код', max_length=13)),
                ('index', models.CharField(db_index=True, blank=True, null=True, verbose_name='Почтовый индекс', max_length=6)),
                ('gninmb', models.CharField(db_index=True, blank=True, null=True, verbose_name='Код ИФНС', max_length=4)),
                ('uno', models.CharField(db_index=True, blank=True, null=True, verbose_name='Код терр-го участка ИФНС', max_length=4)),
                ('ocatd', models.CharField(db_index=True, blank=True, null=True, verbose_name='ОКАТО', max_length=11)),
                ('status', models.CharField(db_index=True, verbose_name='Статус объекта', max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Socrbase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('level', models.CharField(db_index=True, verbose_name='Уровень объекта', max_length=5)),
                ('scname', models.CharField(db_index=True, verbose_name='Сокращенное наименование тип объекта', max_length=10)),
                ('socrname', models.CharField(db_index=True, verbose_name='Полное наименование тип объекта', max_length=29)),
                ('kod_t_st', models.CharField(db_index=True, verbose_name='Код типа объекта', max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, verbose_name='Наименование', max_length=40)),
                ('socr', models.CharField(verbose_name='Сокращенное наименование тип объекта', max_length=10)),
                ('code', models.CharField(db_index=True, verbose_name='Код', max_length=17)),
                ('index', models.CharField(db_index=True, blank=True, null=True, verbose_name='Почтовый индекс', max_length=6)),
                ('gninmb', models.CharField(db_index=True, blank=True, null=True, verbose_name='Код ИФНС', max_length=4)),
                ('uno', models.CharField(db_index=True, blank=True, null=True, verbose_name='Код терр-го участка ИФНС', max_length=4)),
                ('ocatd', models.CharField(db_index=True, blank=True, null=True, verbose_name='ОКАТО', max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
