# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('value', models.CharField(db_index=True, max_length=150, verbose_name='Контакт')),
                ('contact_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип контакта')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('uniemployee', models.IntegerField(db_index=True, verbose_name='УнивСотрудник')),
                ('fullname', models.CharField(db_index=True, max_length=300, verbose_name='ФИО')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('mid_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('department', models.ForeignKey(to='anketa.Department', verbose_name='Подразделение')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Должность')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(to='staff.Position', verbose_name='Должность'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacts',
            name='employee',
            field=models.ForeignKey(to='staff.Employee', verbose_name='Сотрудник'),
            preserve_default=True,
        ),
    ]
