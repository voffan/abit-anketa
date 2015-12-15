# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20150430_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('img_content', models.ImageField(verbose_name='Ваше фото', upload_to='anketa/static/anketa/img/', help_text='150x150px')),
                ('news', models.ForeignKey(verbose_name='Название новости', to='staff.News')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
