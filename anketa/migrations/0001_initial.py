# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kladr', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abiturient_attrs',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('zipcode', models.CharField(max_length=6, null=True, blank=True, verbose_name='Индекс')),
                ('house', models.CharField(max_length=5, verbose_name='дом')),
                ('building', models.CharField(max_length=5, null=True, blank=True, verbose_name='корпус')),
                ('flat', models.CharField(max_length=5, null=True, blank=True, verbose_name='квартира')),
                ('adrs_type_same', models.BooleanField(default=False, verbose_name='Адрес по прописке совпадает с адресом фактического проживания')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='Дата подачи', auto_now_add=True, db_index=True)),
                ('number', models.IntegerField(max_length=10, null=True, blank=True, verbose_name='Номер заявления')),
                ('budget', models.BooleanField(default=False, verbose_name='В рамках контрольных цифр приёма')),
                ('withfee', models.BooleanField(default=False, verbose_name='по договорам об оказании платных обр. услуг')),
                ('points', models.IntegerField(verbose_name='Кол-во баллов', db_index=True)),
                ('priority', models.CharField(max_length=10, default='В', blank=True, null=True, choices=[('В', 'Высокий'), ('С', 'Средний'), ('Н', 'Низкий')], verbose_name='Приоритет')),
                ('track', models.BooleanField(default=True, verbose_name='Отслеживание')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application_attrs',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('app', models.ForeignKey(verbose_name='Заявление', to='anketa.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='Наименование атрибута', db_index=True)),
                ('parent', models.ForeignKey(blank=True, null=True, to='anketa.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttrValue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=250, verbose_name='Значение', db_index=True)),
                ('attribute', models.ForeignKey(verbose_name='Атрибут', to='anketa.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=200, verbose_name='Контакт')),
                ('contact_type', models.ForeignKey(related_name='ContactTypeAnketa', verbose_name='Тип контакта', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepAchieves',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('points', models.IntegerField(verbose_name='Баллы')),
                ('contest', models.ForeignKey(related_name='contest_dep', verbose_name='Мероприятие', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=200, verbose_name='Значение атрибута')),
                ('attr', models.ForeignKey(related_name='Attrname', verbose_name='Наименование атрибута', to='anketa.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('serialno', models.IntegerField(max_length=15, null=True, blank=True, db_index=True, verbose_name='Серия документа')),
                ('number', models.IntegerField(max_length=15, null=True, blank=True, db_index=True, verbose_name='Номер документа')),
                ('issueDate', models.DateField(null=True, blank=True, verbose_name='Дата выдачи')),
                ('isCopy', models.BooleanField(default=False, verbose_name='Оригинал документа')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('enterDate', models.DateField(verbose_name='Дата поступления')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education_Prog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Направление/специальность', db_index=True)),
                ('duration', models.ForeignKey(related_name='duration\t', blank=True, null=True, verbose_name='Срок обучения', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EduOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Образовательное учреждение', db_index=True)),
                ('head', models.ForeignKey(blank=True, null=True, to='anketa.EduOrg')),
                ('orgtype', models.ForeignKey(blank=True, null=True, verbose_name='Тип образовательного учреждения', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('points', models.IntegerField(max_length=3, null=True, blank=True, db_index=True, verbose_name='Кол-во баллов')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('min_points', models.IntegerField(verbose_name='Мин-ое кол-во баллов')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NeedDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('docType', models.ForeignKey(related_name='DocType_need', verbose_name='Тип документа', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('fname', models.CharField(max_length=30, verbose_name='Имя')),
                ('mname', models.CharField(max_length=30, verbose_name='Отчество')),
                ('fullname', models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name='ФИО')),
                ('sex', models.CharField(max_length=1, default='М', choices=[('М', 'Мужской'), ('Ж', 'Женский')], verbose_name='Пол')),
                ('birthdate', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Abiturient',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='anketa.Person', serialize=False)),
                ('birthplace', models.CharField(max_length=100, null=True, blank=True, verbose_name='Место рождения')),
                ('hostel', models.NullBooleanField(default=False, verbose_name='Требуется общежитие')),
                ('token', models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name='Token')),
                ('info_progress', models.CharField(max_length=20, null=True, blank=True, verbose_name='Progress')),
                ('work_duration', models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name='Трудовой стаж')),
            ],
            options={
            },
            bases=('anketa.person',),
        ),
        migrations.CreateModel(
            name='Milit',
            fields=[
                ('abiturient', models.OneToOneField(primary_key=True, to='anketa.Abiturient', verbose_name='Абитуриент', serialize=False)),
                ('liableForMilit', models.BooleanField(default=False, verbose_name='Военнообязанный')),
                ('isServed', models.BooleanField(default=False, verbose_name='служил в армии')),
                ('yearDismissial', models.IntegerField(max_length=4, null=True, blank=True, verbose_name='Год увольнения из рядов РА')),
                ('rank', models.ForeignKey(related_name='Rank', blank=True, null=True, verbose_name='Воинское звание', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Privilegies',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('abiturient', models.ForeignKey(verbose_name='Абитуриент', to='anketa.Abiturient')),
                ('category', models.ForeignKey(related_name='Category', verbose_name='Категория', to='anketa.AttrValue')),
                ('priv_type', models.ForeignKey(related_name='Priv_type', verbose_name='Тип привелегии', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('freespaces', models.IntegerField(verbose_name='КЦП')),
                ('eduform', models.CharField(max_length=10, default='О', blank=True, null=True, choices=[('О', 'Очное'), ('З', 'Заочное'), ('ОЗ', 'Очно-заочное')], verbose_name='Форма обучения')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('abiturient', models.ForeignKey(related_name='RelationAbiturient', verbose_name='Абитуриент', to='anketa.Abiturient')),
                ('person', models.ForeignKey(related_name='RelationPerson', verbose_name='Родственник', to='anketa.Person')),
                ('relType', models.ForeignKey(verbose_name='Тип связи', to='anketa.AttrValue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Шаблон', db_index=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
            field=models.ForeignKey(related_name='Subject', verbose_name='Дисциплина', to='anketa.AttrValue'),
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
            field=models.ForeignKey(related_name='ExamType', verbose_name='Тип экзамена', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exams',
            name='exam_subjects',
            field=models.ForeignKey(related_name='Exam_Subjects', verbose_name='Дисциплина', to='anketa.AttrValue'),
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
            field=models.ForeignKey(related_name='qualification', verbose_name='Квалификация', to='anketa.AttrValue'),
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
            field=models.ForeignKey(related_name='DocIssuer', verbose_name='Орган выдавший документ', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docs',
            name='docType',
            field=models.ForeignKey(related_name='DocType_docs', verbose_name='Тип документа', to='anketa.AttrValue'),
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
            field=models.ForeignKey(related_name='contest_result_dep', verbose_name='Достигнутый результат', to='anketa.AttrValue'),
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
            field=models.ForeignKey(related_name='Adrs_type', verbose_name='Тип адреса', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(related_name='Street', verbose_name='Улица', to='kladr.Street'),
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
            field=models.ForeignKey(related_name='contest_achievement', verbose_name='Мероприятие', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievements',
            name='result',
            field=models.ForeignKey(related_name='contest_result_achievement', verbose_name='Достигнутый результат', to='anketa.AttrValue'),
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
            field=models.ForeignKey(related_name='Citizenship', blank=True, null=True, verbose_name='Гражданство', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='foreign_lang',
            field=models.ForeignKey(related_name='Foreign', blank=True, null=True, verbose_name='Изучаемый иностранный язык', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='nationality',
            field=models.ForeignKey(related_name='Nationality', blank=True, null=True, verbose_name='Национальность(по желанию)', to='anketa.AttrValue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abiturient',
            name='user',
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
