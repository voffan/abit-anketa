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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(verbose_name='Индекс', max_length=6, blank=True, null=True)),
                ('house', models.CharField(verbose_name='дом', max_length=5)),
                ('building', models.CharField(verbose_name='корпус', max_length=5, blank=True, null=True)),
                ('flat', models.CharField(verbose_name='квартира', max_length=5, blank=True, null=True)),
                ('adrs_type_same', models.BooleanField(default=False, verbose_name='Адрес по прописке совпадает с адресом фактического проживания')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата подачи', db_index=True)),
                ('number', models.IntegerField(verbose_name='Номер заявления', max_length=10, blank=True, null=True)),
                ('budget', models.BooleanField(default=False, verbose_name='В рамках контрольных цифр приёма')),
                ('withfee', models.BooleanField(default=False, verbose_name='по договорам об оказании платных обр. услуг')),
                ('points', models.IntegerField(verbose_name='Кол-во баллов', db_index=True)),
                ('priority', models.CharField(default='В', choices=[('В', 'Высокий'), ('С', 'Средний'), ('Н', 'Низкий')], null=True, verbose_name='Приоритет', max_length=10, blank=True)),
                ('track', models.BooleanField(default=True, verbose_name='Отслеживание')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application_attrs',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('app', models.ForeignKey(verbose_name='Заявление', to='anketa.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationProfiles',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Наименование атрибута', max_length=250, db_index=True)),
                ('parent', models.ForeignKey(null=True, to='anketa.Attribute', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrValue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('value', models.CharField(verbose_name='Значение', max_length=250, db_index=True)),
                ('attribute', models.ForeignKey(verbose_name='Атрибут', to='anketa.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('value', models.CharField(verbose_name='Контакт', max_length=200)),
                ('contact_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип контакта', related_name='ContactTypeAnketa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepAchieves',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('points', models.IntegerField(verbose_name='Баллы')),
                ('contest', models.ForeignKey(to='anketa.AttrValue', verbose_name='Мероприятие', related_name='contest_dep')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocAttr',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('value', models.CharField(verbose_name='Значение атрибута', max_length=200)),
                ('attr', models.ForeignKey(to='anketa.Attribute', verbose_name='Наименование атрибута', related_name='Attrname')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('serialno', models.IntegerField(verbose_name='Серия документа', max_length=15, blank=True, db_index=True, null=True)),
                ('number', models.IntegerField(verbose_name='Номер документа', max_length=15, blank=True, db_index=True, null=True)),
                ('issueDate', models.DateField(verbose_name='Дата выдачи', blank=True, null=True)),
                ('isCopy', models.BooleanField(default=False, verbose_name='Оригинал документа')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('enterDate', models.DateField(verbose_name='Дата поступления')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education_Prog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Направление/специальность', max_length=200, db_index=True)),
                ('duration', models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Срок обучения', related_name='duration\t', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EduOrg',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Образовательное учреждение', max_length=100, db_index=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('points', models.IntegerField(verbose_name='Кол-во баллов', max_length=3, blank=True, db_index=True, null=True)),
                ('year', models.IntegerField(verbose_name='Год', max_length=4)),
                ('special', models.BooleanField(default=False, verbose_name='Особые условия')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exams_needed',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('min_points', models.IntegerField(verbose_name='Мин-ое кол-во баллов')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NeedDocuments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('docType', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип документа', related_name='DocType_need')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('sname', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('fname', models.CharField(verbose_name='Имя', max_length=30)),
                ('mname', models.CharField(verbose_name='Отчество', max_length=30)),
                ('fullname', models.CharField(verbose_name='ФИО', max_length=200, blank=True, db_index=True, null=True)),
                ('sex', models.CharField(default='М', verbose_name='Пол', max_length=1, choices=[('М', 'Мужской'), ('Ж', 'Женский')])),
                ('birthdate', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Abiturient',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, to='anketa.Person', primary_key=True, parent_link=True, serialize=False)),
                ('birthplace', models.CharField(verbose_name='Место рождения', max_length=100, blank=True, null=True)),
                ('hostel', models.NullBooleanField(default=False, verbose_name='Требуется общежитие')),
                ('token', models.CharField(verbose_name='Token', max_length=100, blank=True, db_index=True, null=True)),
                ('info_progress', models.CharField(verbose_name='Progress', max_length=20, blank=True, null=True)),
                ('work_duration', models.CharField(verbose_name='Трудовой стаж', max_length=100, blank=True, db_index=True, null=True)),
            ],
            options={
            },
            bases=('anketa.person',),
        ),
        migrations.CreateModel(
            name='Milit',
            fields=[
                ('abiturient', models.OneToOneField(to='anketa.Abiturient', primary_key=True, serialize=False, verbose_name='Абитуриент')),
                ('liableForMilit', models.BooleanField(default=False, verbose_name='Военнообязанный')),
                ('isServed', models.BooleanField(default=False, verbose_name='служил в армии')),
                ('yearDismissial', models.IntegerField(verbose_name='Год увольнения из рядов РА', max_length=4, blank=True, null=True)),
                ('rank', models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Воинское звание', related_name='Rank', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Privilegies',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('abiturient', models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient')),
                ('category', models.ForeignKey(to='anketa.AttrValue', verbose_name='Категория', related_name='Category')),
                ('priv_type', models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип привелегии', related_name='Priv_type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Профиль', max_length=100, db_index=True)),
                ('edu_prog', models.ForeignKey(to='anketa.Education_Prog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileAttrs',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('freespaces', models.IntegerField(verbose_name='КЦП')),
                ('eduform', models.CharField(default='О', choices=[('О', 'Очное'), ('З', 'Заочное'), ('ОЗ', 'Очно-заочное')], null=True, verbose_name='Форма обучения', max_length=10, blank=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('abiturient', models.ForeignKey(to='anketa.Abiturient', verbose_name='Абитуриент', related_name='RelationAbiturient')),
                ('person', models.ForeignKey(to='anketa.Person', verbose_name='Родственник', related_name='RelationPerson')),
                ('relType', models.ForeignKey(verbose_name='Тип связи', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Шаблон', max_length=200, db_index=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Дисциплина', related_name='Subject'),
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
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип экзамена', related_name='ExamType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='exam_subjects',
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Дисциплина', related_name='Exam_Subjects'),
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
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Квалификация', related_name='qualification'),
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
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Орган выдавший документ', related_name='DocIssuer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='docType',
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип документа', related_name='DocType_docs'),
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
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Достигнутый результат', related_name='contest_result_dep'),
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
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Тип адреса', related_name='Adrs_type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(to='kladr.Street', verbose_name='Улица', related_name='Street'),
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
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Мероприятие', related_name='contest_achievement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='result',
            field=models.ForeignKey(to='anketa.AttrValue', verbose_name='Достигнутый результат', related_name='contest_result_achievement'),
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
            field=models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Гражданство', related_name='Citizenship', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='foreign_lang',
            field=models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Изучаемый иностранный язык', related_name='Foreign', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='nationality',
            field=models.ForeignKey(null=True, to='anketa.AttrValue', verbose_name='Национальность(по желанию)', related_name='Nationality', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='user',
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
