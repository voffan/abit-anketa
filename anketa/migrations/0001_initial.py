# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('kladr', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kladr', '__first__'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
    ]

    operations = [
        migrations.CreateModel(
            name='Abiturient_attrs',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(verbose_name='Индекс', max_length=6, blank=True, null=True)),
                ('house', models.CharField(verbose_name='дом', max_length=5)),
                ('building', models.CharField(verbose_name='корпус', max_length=5, blank=True, null=True)),
                ('flat', models.CharField(verbose_name='квартира', max_length=5, blank=True, null=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('zipcode', models.CharField(max_length=6, null=True, blank=True, verbose_name='Индекс')),
                ('house', models.CharField(max_length=5, verbose_name='дом')),
                ('building', models.CharField(max_length=5, null=True, blank=True, verbose_name='корпус')),
                ('flat', models.CharField(max_length=5, null=True, blank=True, verbose_name='квартира')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('adrs_type_same', models.BooleanField(default=False, verbose_name='Адрес по прописке совпадает с адресом фактического проживания')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата подачи', db_index=True)),
                ('number', models.IntegerField(verbose_name='Номер заявления', max_length=10, blank=True, null=True)),
                ('budget', models.BooleanField(default=False, verbose_name='В рамках контрольных цифр приёма')),
                ('withfee', models.BooleanField(default=False, verbose_name='по договорам об оказании платных обр. услуг')),
                ('points', models.IntegerField(verbose_name='Кол-во баллов', db_index=True)),
                ('priority', models.CharField(default='В', choices=[('В', 'Высокий'), ('С', 'Средний'), ('Н', 'Низкий')], null=True, verbose_name='Приоритет', max_length=10, blank=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='Дата подачи', auto_now_add=True, db_index=True)),
                ('number', models.IntegerField(max_length=10, null=True, blank=True, verbose_name='Номер заявления')),
                ('budget', models.BooleanField(default=False, verbose_name='В рамках контрольных цифр приёма')),
                ('withfee', models.BooleanField(default=False, verbose_name='по договорам об оказании платных обр. услуг')),
                ('points', models.IntegerField(verbose_name='Кол-во баллов', db_index=True)),
                ('priority', models.CharField(max_length=10, default='В', blank=True, null=True, choices=[('В', 'Высокий'), ('С', 'Средний'), ('Н', 'Низкий')], verbose_name='Приоритет')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('track', models.BooleanField(default=True, verbose_name='Отслеживание')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application_attrs',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('app', models.ForeignKey(verbose_name='Заявление', to='anketa.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationProfiles',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('points', models.IntegerField(verbose_name='Кол-во баллов')),
                ('application', models.ForeignKey(verbose_name='Заявление', to='anketa.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Наименование атрибута', max_length=250, db_index=True)),
                ('parent', models.ForeignKey(null=True, to='anketa.Attribute', blank=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='Наименование атрибута', db_index=True)),
                ('parent', models.ForeignKey(blank=True, null=True, to='anketa.Attribute')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrType',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='', max_length=100)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrValue',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('value', models.CharField(verbose_name='Значение', max_length=250, db_index=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=250, verbose_name='Значение', db_index=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('attribute', models.ForeignKey(verbose_name='Атрибут', to='anketa.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('value', models.CharField(verbose_name='Контакт', max_length=200)),
                ('contact_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип контакта', related_name='ContactTypeAnketa')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=200, verbose_name='Контакт')),
                ('contact_type', models.ForeignKey(related_name='ContactTypeAnketa', verbose_name='Тип контакта', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepAchieves',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('points', models.IntegerField(verbose_name='Баллы')),
                ('contest', models.ForeignKey(to='anketa.AttrValue', verbose_name='Мероприятие', related_name='contest_dep')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('points', models.IntegerField(verbose_name='Баллы')),
                ('contest', models.ForeignKey(related_name='contest_dep', verbose_name='Мероприятие', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocAttr',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('value', models.CharField(verbose_name='Значение атрибута', max_length=200)),
                ('attr', models.ForeignKey(to='anketa.Attribute', verbose_name='Наименование атрибута', related_name='Attrname')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=200, verbose_name='Значение атрибута')),
                ('attr', models.ForeignKey(related_name='Attrname', verbose_name='Наименование атрибута', to='anketa.Attribute')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('serialno', models.IntegerField(verbose_name='Серия документа', max_length=15, blank=True, db_index=True, null=True)),
                ('number', models.IntegerField(verbose_name='Номер документа', max_length=15, blank=True, db_index=True, null=True)),
                ('issueDate', models.DateField(verbose_name='Дата выдачи', blank=True, null=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('serialno', models.IntegerField(max_length=15, null=True, blank=True, db_index=True, verbose_name='Серия документа')),
                ('number', models.IntegerField(max_length=15, null=True, blank=True, db_index=True, verbose_name='Номер документа')),
                ('issueDate', models.DateField(null=True, blank=True, verbose_name='Дата выдачи')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('isCopy', models.BooleanField(default=False, verbose_name='Оригинал документа')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('enterDate', models.DateField(verbose_name='Дата поступления')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education_Prog',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Направление/специальность', max_length=200, db_index=True)),
                ('duration', models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Срок обучения', related_name='duration\t', blank=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Направление/специальность', db_index=True)),
                ('duration', models.ForeignKey(related_name='duration\t', blank=True, null=True, verbose_name='Срок обучения', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EduOrg',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Образовательное учреждение', max_length=100, db_index=True)),
                ('head', models.ForeignKey(null=True, to='anketa.EduOrg', blank=True)),
                ('orgtype', models.ForeignKey(null=True, verbose_name='Тип образовательного учреждения', to='anketa.AttrValue', blank=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Образовательное учреждение', db_index=True)),
                ('head', models.ForeignKey(blank=True, null=True, to='anketa.EduOrg')),
                ('orgtype', models.ForeignKey(blank=True, null=True, verbose_name='Тип образовательного учреждения', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('points', models.IntegerField(verbose_name='Кол-во баллов', max_length=3, blank=True, db_index=True, null=True)),
                ('year', models.IntegerField(verbose_name='Год', max_length=4)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('points', models.IntegerField(max_length=3, null=True, blank=True, db_index=True, verbose_name='Кол-во баллов')),
                ('year', models.IntegerField(max_length=4, verbose_name='Год')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('special', models.BooleanField(default=False, verbose_name='Особые условия')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exams_needed',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('min_points', models.IntegerField(verbose_name='Мин-ое кол-во баллов')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NeedDocuments',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('docType', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип документа', related_name='DocType_need')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('docType', models.ForeignKey(related_name='DocType_need', verbose_name='Тип документа', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('sname', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('fname', models.CharField(verbose_name='Имя', max_length=30)),
                ('mname', models.CharField(verbose_name='Отчество', max_length=30)),
                ('fullname', models.CharField(verbose_name='ФИО', max_length=200, blank=True, db_index=True, null=True)),
                ('sex', models.CharField(default='М', verbose_name='Пол', max_length=1, choices=[('М', 'Мужской'), ('Ж', 'Женский')])),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('fname', models.CharField(max_length=30, verbose_name='Имя')),
                ('mname', models.CharField(max_length=30, verbose_name='Отчество')),
                ('fullname', models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name='ФИО')),
                ('sex', models.CharField(max_length=1, default='М', choices=[('М', 'Мужской'), ('Ж', 'Женский')], verbose_name='Пол')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('birthdate', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Abiturient',
            fields=[
<<<<<<< HEAD
                ('person_ptr', models.OneToOneField(auto_created=True, to='anketa.Person', primary_key=True, parent_link=True, serialize=False)),
                ('birthplace', models.CharField(verbose_name='Место рождения', max_length=100, blank=True, null=True)),
                ('hostel', models.NullBooleanField(default=False, verbose_name='Требуется общежитие')),
                ('token', models.CharField(verbose_name='Token', max_length=100, blank=True, db_index=True, null=True)),
                ('info_progress', models.CharField(verbose_name='Progress', max_length=20, blank=True, null=True)),
                ('work_duration', models.CharField(verbose_name='Трудовой стаж', max_length=100, blank=True, db_index=True, null=True)),
=======
                ('person_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='anketa.Person', serialize=False)),
                ('birthplace', models.CharField(max_length=100, null=True, blank=True, verbose_name='Место рождения')),
                ('hostel', models.NullBooleanField(default=False, verbose_name='Требуется общежитие')),
                ('token', models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name='Token')),
                ('info_progress', models.CharField(max_length=20, null=True, blank=True, verbose_name='Progress')),
                ('work_duration', models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name='Трудовой стаж')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=('anketa.person',),
        ),
        migrations.CreateModel(
            name='Milit',
            fields=[
<<<<<<< HEAD
                ('abiturient', models.OneToOneField(to='anketa.Abiturient', primary_key=True, serialize=False, verbose_name='Абитуриент')),
                ('liableForMilit', models.BooleanField(default=False, verbose_name='Военнообязанный')),
                ('isServed', models.BooleanField(default=False, verbose_name='служил в армии')),
                ('yearDismissial', models.IntegerField(verbose_name='Год увольнения из рядов РА', max_length=4, blank=True, null=True)),
                ('rank', models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Воинское звание', related_name='Rank', blank=True)),
=======
                ('abiturient', models.OneToOneField(primary_key=True, to='anketa.Abiturient', verbose_name='Абитуриент', serialize=False)),
                ('liableForMilit', models.BooleanField(default=False, verbose_name='Военнообязанный')),
                ('isServed', models.BooleanField(default=False, verbose_name='служил в армии')),
                ('yearDismissial', models.IntegerField(max_length=4, null=True, blank=True, verbose_name='Год увольнения из рядов РА')),
                ('rank', models.ForeignKey(related_name='Rank', blank=True, null=True, verbose_name='Воинское звание', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Privilegies',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('abiturient', models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient')),
                ('category', models.ForeignKey(to='anketa.AttrValue', verbose_name='Категория', related_name='Category')),
                ('priv_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип привелегии', related_name='Priv_type')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('abiturient', models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient')),
                ('category', models.ForeignKey(related_name='Category', verbose_name='Категория', to='anketa.AttrValue')),
                ('priv_type', models.ForeignKey(related_name='Priv_type', verbose_name='Тип привелегии', to='anketa.AttrValue')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Профиль', max_length=100, db_index=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Профиль', db_index=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('edu_prog', models.ForeignKey(to='anketa.Education_Prog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileAttrs',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('freespaces', models.IntegerField(verbose_name='КЦП')),
                ('eduform', models.CharField(default='О', choices=[('О', 'Очное'), ('З', 'Заочное'), ('ОЗ', 'Очно-заочное')], null=True, verbose_name='Форма обучения', max_length=10, blank=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('freespaces', models.IntegerField(verbose_name='КЦП')),
                ('eduform', models.CharField(max_length=10, default='О', blank=True, null=True, choices=[('О', 'Очное'), ('З', 'Заочное'), ('ОЗ', 'Очно-заочное')], verbose_name='Форма обучения')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('year', models.IntegerField(verbose_name='Год')),
                ('startDate', models.DateField(verbose_name='Дата начала приемной кампании')),
                ('endDate', models.DateField(verbose_name='Дата конца приемной кампании')),
                ('profile', models.ForeignKey(to='anketa.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('abiturient', models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент', related_name='RelationAbiturient')),
                ('person', models.ForeignKey(to='anketa.Person', verbose_name='Родственник', related_name='RelationPerson')),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('abiturient', models.ForeignKey(related_name='RelationAbiturient', verbose_name='Абитуриент', to='anketa.Abiturient')),
                ('person', models.ForeignKey(related_name='RelationPerson', verbose_name='Родственник', to='anketa.Person')),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('relType', models.ForeignKey(verbose_name='Тип связи', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Шаблон', max_length=200, db_index=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Шаблон', db_index=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('active', models.BooleanField(default=True, verbose_name='Активно')),
                ('org', models.ForeignKey(verbose_name='Обр. учреждение', to='anketa.EduOrg')),
                ('type', models.ForeignKey(verbose_name='Тип шаблона', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateAttrs',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
                ('attribute', models.ForeignKey(verbose_name='Атрибут', to='anketa.Attribute')),
                ('template', models.ForeignKey(verbose_name='Обр. учреждение', to='anketa.Template')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='needdocuments',
            name='profile',
            field=models.ForeignKey(verbose_name='Профиль', to='anketa.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams_needed',
            name='profile',
            field=models.ForeignKey(verbose_name='Профиль', to='anketa.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams_needed',
            name='subject',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Дисциплина', related_name='Subject'),
=======
            field=models.ForeignKey(related_name='Subject', verbose_name='Дисциплина', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='abiturient',
            field=models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='exam_examType',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип экзамена', related_name='ExamType'),
=======
            field=models.ForeignKey(related_name='ExamType', verbose_name='Тип экзамена', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='exam_subjects',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Дисциплина', related_name='Exam_Subjects'),
=======
            field=models.ForeignKey(related_name='Exam_Subjects', verbose_name='Дисциплина', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education_prog',
            name='eduorg',
            field=models.ForeignKey(verbose_name='Образовательное учреждение', to='anketa.EduOrg'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education_prog',
            name='qualification',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Квалификация', related_name='qualification'),
=======
            field=models.ForeignKey(related_name='qualification', verbose_name='Квалификация', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='abiturient',
            field=models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='doc',
            field=models.ForeignKey(verbose_name='Документ', to='anketa.Docs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='level',
            field=models.ForeignKey(verbose_name='Уровень образования', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='abiturient',
            field=models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='docIssuer',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Орган выдавший документ', related_name='DocIssuer'),
=======
            field=models.ForeignKey(related_name='DocIssuer', verbose_name='Орган выдавший документ', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='docType',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип документа', related_name='DocType_docs'),
=======
            field=models.ForeignKey(related_name='DocType_docs', verbose_name='Тип документа', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docattr',
            name='doc',
            field=models.ForeignKey(verbose_name='Документ', to='anketa.Docs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depachieves',
            name='profile',
            field=models.ForeignKey(verbose_name='Профиль', to='anketa.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depachieves',
            name='result',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Достигнутый результат', related_name='contest_result_dep'),
=======
            field=models.ForeignKey(related_name='contest_result_dep', verbose_name='Достигнутый результат', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacts',
            name='person',
            field=models.ForeignKey(verbose_name='Человек', to='anketa.Person'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attrvalue',
            unique_together=set([('attribute', 'value')]),
        ),
        migrations.AddField(
            model_name='attribute',
            name='type',
            field=models.ForeignKey(verbose_name='Тип атрибута', to='anketa.AttrType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('type', 'name')]),
        ),
        migrations.AddField(
            model_name='applicationprofiles',
            name='profile',
            field=models.ForeignKey(verbose_name='Профиль направления', to='anketa.ProfileAttrs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application_attrs',
            name='attribute',
            field=models.ForeignKey(verbose_name='Атрибут', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='abiturient',
            field=models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='appState',
            field=models.ForeignKey(verbose_name='Состояние заявления', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='department',
            field=models.ForeignKey(verbose_name='Институт/факультет', to='anketa.EduOrg'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='abiturient',
            field=models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='adrs_type',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип адреса', related_name='Adrs_type'),
=======
            field=models.ForeignKey(related_name='Adrs_type', verbose_name='Тип адреса', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='street',
<<<<<<< HEAD
            field=models.ForeignKey(to='kladr.Street', verbose_name='Улица', related_name='Street'),
=======
            field=models.ForeignKey(related_name='Street', verbose_name='Улица', to='kladr.Street'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='abiturient',
            field=models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='contest',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Мероприятие', related_name='contest_achievement'),
=======
            field=models.ForeignKey(related_name='contest_achievement', verbose_name='Мероприятие', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='result',
<<<<<<< HEAD
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Достигнутый результат', related_name='contest_result_achievement'),
=======
            field=models.ForeignKey(related_name='contest_result_achievement', verbose_name='Достигнутый результат', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient_attrs',
            name='abiturient',
            field=models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient_attrs',
            name='attribute',
            field=models.ForeignKey(verbose_name='Атрибут', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='citizenship',
<<<<<<< HEAD
            field=models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Гражданство', related_name='Citizenship', blank=True),
=======
            field=models.ForeignKey(related_name='Citizenship', blank=True, null=True, verbose_name='Гражданство', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='foreign_lang',
<<<<<<< HEAD
            field=models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Изучаемый иностранный язык', related_name='Foreign', blank=True),
=======
            field=models.ForeignKey(related_name='Foreign', blank=True, null=True, verbose_name='Изучаемый иностранный язык', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='nationality',
<<<<<<< HEAD
            field=models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Национальность(по желанию)', related_name='Nationality', blank=True),
=======
            field=models.ForeignKey(related_name='Nationality', blank=True, null=True, verbose_name='Национальность(по желанию)', to='anketa.AttrValue'),
>>>>>>> 6ad375485a5f29b45d53f492899989317beb1e2e
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='user',
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
