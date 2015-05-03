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
            name='EmplContacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(db_index=True, max_length=150, verbose_name='Контакт')),
                ('contact_type', models.ForeignKey(to='anketa.Attribute', verbose_name='Тип контакта')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=100, verbose_name='Фамилия')),
                ('last_name', models.CharField(db_index=True, max_length=100, verbose_name='Имя')),
                ('middle_name', models.CharField(db_index=True, max_length=100, verbose_name='Отчество')),
                ('fullname', models.CharField(db_index=True, max_length=300, verbose_name='ФИО')),
                ('position', models.CharField(max_length=200, verbose_name='Должность')),
                ('department', models.ForeignKey(to='anketa.Department', verbose_name='Подразделение')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('NewsName', models.CharField(max_length=30, verbose_name='Название новости')),
                ('Description', models.CharField(max_length=100, verbose_name='Описание')),
                ('NewsDate', models.DateField(db_index=True, verbose_name='Дата новости')),
                ('NewsText', models.CharField(max_length=3000, verbose_name='Контент')),
                ('employee', models.ForeignKey(to='staff.Employee', verbose_name='Автор')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='emplcontacts',
            name='employee',
            field=models.ForeignKey(to='staff.Employee', verbose_name='Сотрудник'),
            preserve_default=True,
        ),
    ]
