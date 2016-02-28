# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anketa', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=150, verbose_name='Контакт', db_index=True)),
                ('contact_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип контакта')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('uniemployee', models.IntegerField(verbose_name='УнивСотрудник', db_index=True)),
                ('fullname', models.CharField(max_length=300, verbose_name='ФИО', db_index=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Должность', db_index=True)),
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
