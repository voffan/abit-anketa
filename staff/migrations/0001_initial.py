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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.CharField(verbose_name='Контакт', db_index=True, max_length=150)),
                ('contact_type', models.ForeignKey(verbose_name='Тип контакта', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uniemployee', models.IntegerField(verbose_name='УнивСотрудник', db_index=True)),
                ('fullname', models.CharField(verbose_name='ФИО', db_index=True, max_length=300)),
                ('first_name', models.CharField(verbose_name='Фамилия', max_length=100)),
                ('mid_name', models.CharField(verbose_name='Имя', max_length=100)),
                ('last_name', models.CharField(verbose_name='Отчество', max_length=100)),
                ('department', models.ForeignKey(verbose_name='Подразделение', to='anketa.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Должность', db_index=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(verbose_name='Должность', to='staff.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacts',
            name='employee',
            field=models.ForeignKey(verbose_name='Сотрудник', to='staff.Employee'),
            preserve_default=True,
        ),
    ]
