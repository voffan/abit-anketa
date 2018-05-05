# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anketa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(verbose_name='Контакт', max_length=150, db_index=True)),
                ('contact_type', models.ForeignKey(verbose_name='Тип контакта', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('uniemployee', models.IntegerField(verbose_name='УнивСотрудник', db_index=True)),
                ('fullname', models.CharField(verbose_name='ФИО', null=True, max_length=200, db_index=True, blank=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('mid_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('department', models.ForeignKey(verbose_name='Подразделение', to='anketa.EduOrg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Должность', max_length=200, db_index=True)),
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
