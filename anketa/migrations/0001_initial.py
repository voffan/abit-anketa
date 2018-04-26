# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('kladr', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Abiturient_attrs',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('zipcode', models.CharField(blank=True, max_length=6, verbose_name='Индекс', null=True)),
                ('house', models.CharField(max_length=5, verbose_name='дом')),
                ('building', models.CharField(blank=True, max_length=5, verbose_name='корпус', null=True)),
                ('flat', models.CharField(blank=True, max_length=5, verbose_name='квартира', null=True)),
                ('adrs_type_same', models.BooleanField(default=False, verbose_name='Адрес по прописке совпадает с адресом фактического проживания')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата подачи', db_index=True)),
                ('number', models.IntegerField(blank=True, max_length=10, verbose_name='Номер заявления', null=True)),
                ('budget', models.BooleanField(default=False, verbose_name='В рамках контрольных цифр приёма')),
                ('withfee', models.BooleanField(default=False, verbose_name='по договорам об оказании платных обр. услуг')),
                ('points', models.IntegerField(verbose_name='Кол-во баллов', db_index=True)),
                ('priority', models.CharField(max_length=10, default='В', null=True, verbose_name='Приоритет', blank=True, choices=[('В', 'Высокий'), ('С', 'Средний'), ('Н', 'Низкий')])),
                ('track', models.BooleanField(default=True, verbose_name='Отслеживание')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application_attrs',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('app', models.ForeignKey(to='anketa.Application', verbose_name='Заявление')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationProfiles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('points', models.IntegerField(verbose_name='Кол-во баллов')),
                ('application', models.ForeignKey(to='anketa.Application', verbose_name='Заявление')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='Наименование атрибута', db_index=True)),
                ('parent', models.ForeignKey(null=True, to='anketa.Attribute', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrValue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=250, verbose_name='Значение', db_index=True)),
                ('attribute', models.ForeignKey(to='anketa.Attribute', verbose_name='Атрибут')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=200, verbose_name='Контакт')),
                ('contact_type', models.ForeignKey(verbose_name='Тип контакта', to='anketa.AttrValue', related_name='ContactTypeAnketa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepAchieves',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('points', models.IntegerField(verbose_name='Баллы')),
                ('contest', models.ForeignKey(verbose_name='Мероприятие', to='anketa.AttrValue', related_name='contest_dep')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocAttr',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=200, verbose_name='Значение атрибута')),
                ('attr', models.ForeignKey(verbose_name='Наименование атрибута', to='anketa.Attribute', related_name='Attrname')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('serialno', models.IntegerField(blank=True, max_length=15, verbose_name='Серия документа', db_index=True, null=True)),
                ('number', models.IntegerField(blank=True, max_length=15, verbose_name='Номер документа', db_index=True, null=True)),
                ('issueDate', models.DateField(blank=True, verbose_name='Дата выдачи', null=True)),
                ('isCopy', models.BooleanField(default=False, verbose_name='Оригинал документа')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('enterDate', models.DateField(verbose_name='Дата поступления')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education_Prog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Направление/специальность', db_index=True)),
                ('duration', models.ForeignKey(null=True, verbose_name='Срок обучения', to='anketa.AttrValue', blank=True, related_name='duration\t')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EduOrg',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Образовательное учреждение', db_index=True)),
                ('head', models.ForeignKey(null=True, to='anketa.EduOrg', blank=True)),
                ('orgtype', models.ForeignKey(null=True, verbose_name='Тип образовательного учреждения', to='anketa.AttrValue', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('points', models.IntegerField(blank=True, max_length=3, verbose_name='Кол-во баллов', db_index=True, null=True)),
                ('year', models.IntegerField(max_length=4, verbose_name='Год')),
                ('special', models.BooleanField(default=False, verbose_name='Особые условия')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exams_needed',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('min_points', models.IntegerField(verbose_name='Мин-ое кол-во баллов')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NeedDocuments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('docType', models.ForeignKey(verbose_name='Тип документа', to='anketa.AttrValue', related_name='DocType_need')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('sname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('fname', models.CharField(max_length=30, verbose_name='Имя')),
                ('mname', models.CharField(max_length=30, verbose_name='Отчество')),
                ('fullname', models.CharField(blank=True, max_length=200, verbose_name='ФИО', db_index=True, null=True)),
                ('sex', models.CharField(default='М', max_length=1, verbose_name='Пол', choices=[('М', 'Мужской'), ('Ж', 'Женский')])),
                ('birthdate', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Abiturient',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='anketa.Person', serialize=False)),
                ('birthplace', models.CharField(blank=True, max_length=100, verbose_name='Место рождения', null=True)),
                ('hostel', models.NullBooleanField(default=False, verbose_name='Требуется общежитие')),
                ('token', models.CharField(blank=True, max_length=100, verbose_name='Token', db_index=True, null=True)),
                ('info_progress', models.CharField(blank=True, max_length=20, verbose_name='Progress', null=True)),
                ('work_duration', models.CharField(blank=True, max_length=100, verbose_name='Трудовой стаж', db_index=True, null=True)),
            ],
            options={
            },
            bases=('anketa.person',),
        ),
        migrations.CreateModel(
            name='Milit',
            fields=[
                ('abiturient', models.OneToOneField(primary_key=True, verbose_name='Абитуриент', to='anketa.Abiturient', serialize=False)),
                ('liableForMilit', models.BooleanField(default=False, verbose_name='Военнообязанный')),
                ('isServed', models.BooleanField(default=False, verbose_name='служил в армии')),
                ('yearDismissial', models.IntegerField(blank=True, max_length=4, verbose_name='Год увольнения из рядов РА', null=True)),
                ('rank', models.ForeignKey(null=True, verbose_name='Воинское звание', to='anketa.AttrValue', blank=True, related_name='Rank')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Privilegies',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('abiturient', models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент')),
                ('category', models.ForeignKey(verbose_name='Категория', to='anketa.AttrValue', related_name='Category')),
                ('priv_type', models.ForeignKey(verbose_name='Тип привелегии', to='anketa.AttrValue', related_name='Priv_type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Профиль', db_index=True)),
                ('edu_prog', models.ForeignKey(to='anketa.Education_Prog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileAttrs',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('freespaces', models.IntegerField(verbose_name='КЦП')),
                ('eduform', models.CharField(max_length=10, default='О', null=True, verbose_name='Форма обучения', blank=True, choices=[('О', 'Очное'), ('З', 'Заочное'), ('ОЗ', 'Очно-заочное')])),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('abiturient', models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient', related_name='RelationAbiturient')),
                ('person', models.ForeignKey(verbose_name='Родственник', to='anketa.Person', related_name='RelationPerson')),
                ('relType', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип связи')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Шаблон', db_index=True)),
                ('active', models.BooleanField(default=True, verbose_name='Активно')),
                ('org', models.ForeignKey(to='anketa.EduOrg', verbose_name='Обр. учреждение')),
                ('type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип шаблона')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateAttrs',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('attribute', models.ForeignKey(to='anketa.Attribute', verbose_name='Атрибут')),
                ('template', models.ForeignKey(to='anketa.Template', verbose_name='Обр. учреждение')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='needdocuments',
            name='profile',
            field=models.ForeignKey(to='anketa.Profile', verbose_name='Профиль'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams_needed',
            name='profile',
            field=models.ForeignKey(to='anketa.Profile', verbose_name='Профиль'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams_needed',
            name='subject',
            field=models.ForeignKey(verbose_name='Дисциплина', to='anketa.AttrValue', related_name='Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='abiturient',
            field=models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='exam_examType',
            field=models.ForeignKey(verbose_name='Тип экзамена', to='anketa.AttrValue', related_name='ExamType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='exam_subjects',
            field=models.ForeignKey(verbose_name='Дисциплина', to='anketa.AttrValue', related_name='Exam_Subjects'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education_prog',
            name='eduorg',
            field=models.ForeignKey(to='anketa.EduOrg', verbose_name='Образовательное учреждение'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education_prog',
            name='qualification',
            field=models.ForeignKey(verbose_name='Квалификация', to='anketa.AttrValue', related_name='qualification'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='abiturient',
            field=models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='doc',
            field=models.ForeignKey(to='anketa.Docs', verbose_name='Документ'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='level',
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Уровень образования'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='abiturient',
            field=models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='docIssuer',
            field=models.ForeignKey(verbose_name='Орган выдавший документ', to='anketa.AttrValue', related_name='DocIssuer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='docType',
            field=models.ForeignKey(verbose_name='Тип документа', to='anketa.AttrValue', related_name='DocType_docs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docattr',
            name='doc',
            field=models.ForeignKey(to='anketa.Docs', verbose_name='Документ'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depachieves',
            name='profile',
            field=models.ForeignKey(to='anketa.Profile', verbose_name='Профиль'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depachieves',
            name='result',
            field=models.ForeignKey(verbose_name='Достигнутый результат', to='anketa.AttrValue', related_name='contest_result_dep'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacts',
            name='person',
            field=models.ForeignKey(to='anketa.Person', verbose_name='Человек'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attrvalue',
            unique_together=set([('attribute', 'value')]),
        ),
        migrations.AddField(
            model_name='attribute',
            name='type',
            field=models.ForeignKey(to='anketa.AttrType', verbose_name='Тип атрибута'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('type', 'name')]),
        ),
        migrations.AddField(
            model_name='applicationprofiles',
            name='profile',
            field=models.ForeignKey(to='anketa.ProfileAttrs', verbose_name='Профиль направления'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application_attrs',
            name='attribute',
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Атрибут'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='abiturient',
            field=models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='appState',
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Состояние заявления'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='department',
            field=models.ForeignKey(to='anketa.EduOrg', verbose_name='Институт/факультет'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='abiturient',
            field=models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='adrs_type',
            field=models.ForeignKey(verbose_name='Тип адреса', to='anketa.AttrValue', related_name='Adrs_type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(verbose_name='Улица', to='kladr.Street', related_name='Street'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='abiturient',
            field=models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='contest',
            field=models.ForeignKey(verbose_name='Мероприятие', to='anketa.AttrValue', related_name='contest_achievement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='result',
            field=models.ForeignKey(verbose_name='Достигнутый результат', to='anketa.AttrValue', related_name='contest_result_achievement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient_attrs',
            name='abiturient',
            field=models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient_attrs',
            name='attribute',
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Атрибут'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='citizenship',
            field=models.ForeignKey(null=True, verbose_name='Гражданство', to='anketa.AttrValue', blank=True, related_name='Citizenship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='foreign_lang',
            field=models.ForeignKey(null=True, verbose_name='Изучаемый иностранный язык', to='anketa.AttrValue', blank=True, related_name='Foreign'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='nationality',
            field=models.ForeignKey(null=True, verbose_name='Национальность(по желанию)', to='anketa.AttrValue', blank=True, related_name='Nationality'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=True,
        ),
    ]
