# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('anketa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anketa', '0001_initial'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('value', models.CharField(db_index=True, max_length=150, verbose_name='Контакт')),
                ('contact_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип контакта')),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(verbose_name='Контакт', max_length=150, db_index=True)),
                ('contact_type', models.ForeignKey(verbose_name='Тип контакта', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('uniemployee', models.IntegerField(db_index=True, verbose_name='УнивСотрудник')),
                ('fullname', models.CharField(blank=True, null=True, db_index=True, max_length=200, verbose_name='ФИО')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('mid_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('active', models.BooleanField(default=True, verbose_name='Активен')),
                ('department', models.ForeignKey(to='anketa.EduOrg', verbose_name='Подразделение')),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('uniemployee', models.IntegerField(verbose_name='УнивСотрудник', db_index=True)),
                ('fullname', models.CharField(verbose_name='ФИО', null=True, max_length=200, db_index=True, blank=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('mid_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('department', models.ForeignKey(verbose_name='Подразделение', to='anketa.EduOrg')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Должность')),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Должность', max_length=200, db_index=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
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
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
<<<<<<< HEAD
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
=======
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacts',
            name='employee',
<<<<<<< HEAD
            field=models.ForeignKey(to='staff.Employee', verbose_name='Сотрудник'),
=======
            field=models.ForeignKey(verbose_name='Сотрудник', to='staff.Employee'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
    ]
