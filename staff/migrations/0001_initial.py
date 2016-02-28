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
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=150, verbose_name='Контакт', db_index=True)),
                ('contact_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип контакта')),
=======
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.CharField(verbose_name='Контакт', db_index=True, max_length=150)),
                ('contact_type', models.ForeignKey(verbose_name='Тип контакта', to='anketa.AttrValue')),
>>>>>>> b4f4e7fcfe4bfcbc092b241fdcdfab1440398c7b
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('uniemployee', models.IntegerField(verbose_name='УнивСотрудник', db_index=True)),
                ('fullname', models.CharField(max_length=300, verbose_name='ФИО', db_index=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('mid_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('department', models.ForeignKey(to='anketa.Department', verbose_name='Подразделение')),
=======
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uniemployee', models.IntegerField(verbose_name='УнивСотрудник', db_index=True)),
                ('fullname', models.CharField(verbose_name='ФИО', db_index=True, max_length=300)),
                ('first_name', models.CharField(verbose_name='Фамилия', max_length=100)),
                ('mid_name', models.CharField(verbose_name='Имя', max_length=100)),
                ('last_name', models.CharField(verbose_name='Отчество', max_length=100)),
                ('department', models.ForeignKey(verbose_name='Подразделение', to='anketa.Department')),
>>>>>>> b4f4e7fcfe4bfcbc092b241fdcdfab1440398c7b
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Должность', db_index=True)),
=======
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Должность', db_index=True, max_length=200)),
>>>>>>> b4f4e7fcfe4bfcbc092b241fdcdfab1440398c7b
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
<<<<<<< HEAD
            field=models.ForeignKey(to='staff.Position', verbose_name='Должность'),
=======
            field=models.ForeignKey(verbose_name='Должность', to='staff.Position'),
>>>>>>> b4f4e7fcfe4bfcbc092b241fdcdfab1440398c7b
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
<<<<<<< HEAD
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
=======
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
>>>>>>> b4f4e7fcfe4bfcbc092b241fdcdfab1440398c7b
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacts',
            name='employee',
            field=models.ForeignKey(verbose_name='Сотрудник', to='staff.Employee'),
            preserve_default=True,
        ),
    ]
