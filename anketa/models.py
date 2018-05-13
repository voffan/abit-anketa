# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from kladr.models import Street
import os

Sex = (
    (u'М', u'Мужской'),
    (u'Ж', u'Женский'),
)
EduForm = (
    (u'О', u'Очное'),
    (u'З', u'Заочное'),
    (u'ОЗ', u'Очно-заочное')
)
AppPrior = (
    (u'В', u'Высокий'),
    (u'С', u'Средний'),
    (u'Н', u'Низкий')
)


def DocImagePath(instance, filename):
    return os.path.join('docimages', str(instance.doc.abiturient.id), str(instance.doc.id), filename)


class Relation(models.Model):
    person = models.ForeignKey('Person', verbose_name=u'Родственник', related_name="RelationPerson")
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент', related_name="RelationAbiturient", db_index=True)
    relType = models.ForeignKey('AttrValue', verbose_name=u'Тип связи', limit_choices_to={'attribute__name': u'Родственная связь'}, db_index=True)

    def __str__(self):
        return self.person.fullname + ' ' + self.relType.value + ' ' + self.abiturient.fullname


class AttrType(models.Model):
    name = models.CharField(u"", max_length=100)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(u'Наименование атрибута', max_length=250, db_index=True)
    type = models.ForeignKey(AttrType, verbose_name=u'Тип атрибута', db_index=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('type', 'name')


class AttrValue(models.Model):
    value = models.CharField(u'Значение', max_length=250, db_index=True)
    attribute = models.ForeignKey(Attribute, verbose_name=u'Атрибут', db_index=True)

    def __str__(self):
        return self.attribute.name + ' ' + self.value

    class Meta:
        unique_together = ('attribute', 'value')


class Person(models.Model):
    sname = models.CharField(u'Фамилия', max_length=30)
    fname = models.CharField(u'Имя', max_length=30)
    mname = models.CharField(u'Отчество', max_length=30)
    fullname = models.CharField(u'ФИО', max_length=200, blank=True, null=True, db_index=True)
    sex = models.CharField(u'Пол', choices=Sex, max_length=1, default='М')
    birthdate = models.DateField(u'Дата рождения')

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        s = ''
        if len(self.sname) > 0:
            s += self.sname
        if len(self.fname) > 0:
            s += ' ' + self.fname
        if len(self.mname) > 0:
            s += ' ' + self.mname
        self.fullname = s
        super(Person, self).save(*args, **kwargs)


class Abiturient(Person):
    birthplace = models.CharField(u'Место рождения', max_length=100, null=True, blank=True)  # добавить r
    hostel = models.NullBooleanField(u'Требуется общежитие', default=False)
    nationality = models.ForeignKey(AttrValue, verbose_name=u'Национальность(по желанию)',
                                    limit_choices_to={'attribute__name': u'Национальность'}, db_index=True, blank=True,
                                    null=True, related_name='Nationality')
    citizenship = models.ForeignKey(AttrValue, verbose_name=u'Гражданство',
                                    limit_choices_to={'attribute__name': u'Гражданство'}, db_index=True,
                                    related_name='Citizenship', null=True, blank=True)
    foreign_lang = models.ForeignKey(AttrValue, verbose_name=u'Изучаемый иностранный язык',
                                     limit_choices_to={'attribute__name': u'Иностранный язык'}, related_name='Foreign',
                                     null=True, blank=True)
    token = models.CharField(u'Token', max_length=100, db_index=True, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name=u'Пользователь', db_index=True)
    info_progress = models.CharField(u'Progress', max_length=20, null=True,
                                     blank=True)  # Битовая маска отображающая какие группа в личных данных заполнена, а какая нет.
    work_duration = models.CharField(u'Трудовой стаж', max_length=100, null=True, db_index=True, blank=True)


class Abiturient_attrs(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент', db_index=True)
    attribute = models.ForeignKey('AttrValue', verbose_name=u'Атрибут', db_index=True)

    def __str__(self):
        return self.abiturient.fullname + ' ' + self.attribute.name


class Application(models.Model):
    department = models.ForeignKey('EduOrg', verbose_name=u'Институт/факультет', db_index=True)
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент', db_index=True)
    date = models.DateField(u'Дата подачи', auto_now_add=True, db_index=True)
    number = models.IntegerField(u'Номер заявления', max_length=10, null=True,
                                 blank=True)  # номер в журнале в приемной комиссии
    budget = models.BooleanField(u'В рамках контрольных цифр приёма', default=False)
    withfee = models.BooleanField(u'по договорам об оказании платных обр. услуг', default=False)
    appState = models.ForeignKey('AttrValue', verbose_name=u'Состояние заявления',
                                 limit_choices_to={'attribute__name': u'Статус заявления'}, db_index=True)
    points = models.IntegerField(u'Кол-во баллов', db_index=True)
    priority = models.CharField(u'Приоритет', choices=AppPrior, default='В', max_length=10, null=True,
                                blank=True)  # Убрать null, blank
    track = models.BooleanField(u'Отслеживание', default=True)

    def __str__(self):
        return self.abiturient.fullname + ' application#' + str(self.id)


class Application_attrs(models.Model):
    app = models.ForeignKey('Application', verbose_name=u'Заявление', db_index=True)
    attribute = models.ForeignKey('AttrValue', verbose_name=u'Атрибут', db_index=True)

    def __str__(self):
        return self.abiturient.fullname + ' ' + self.attribute.name


class Address(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент')
    adrs_type = models.ForeignKey('AttrValue', verbose_name=u'Тип адреса', related_name='Adrs_type')
    zipcode = models.CharField('Индекс', max_length=6, null=True, blank=True)
    street = models.ForeignKey(Street, verbose_name=u'Улица', related_name='Street')
    house = models.CharField('Дом', max_length=5)
    building = models.CharField('Корпус', max_length=5, null=True, blank=True)
    flat = models.CharField('Квартира', max_length=5, null=True, blank=True)
    adrs_type_same = models.BooleanField(u'Адрес по прописке совпадает с адресом фактического проживания',
                                         default=False)


class Contacts(models.Model):
    person = models.ForeignKey('Person', verbose_name=u'Человек', db_index=True)
    contact_type = models.ForeignKey('AttrValue', verbose_name=u'Тип контакта',
                                     limit_choices_to={'attribute__name': u'Тип контакта'},
                                     related_name="ContactTypeAnketa")
    value = models.CharField(u'Контакт', max_length=200)

    def __str__(self):
        return self.person.fullname + ' ' + self.contact_type.value


class Education(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name='Абитуриент')
    doc = models.ForeignKey('Docs', verbose_name='Документ')
    level = models.ForeignKey('AttrValue', verbose_name='Уровень образования',
                              limit_choices_to={'attribute__name': 'Уровень образования'}, db_index=True)
    enterDate = models.DateField('Дата поступления')
    graduationDate = models.DateField('Дата окончания')

    def __str__(self):
        return self.abiturient.fullname + ' ' + str(self.level)


class DocAttr(models.Model):
    doc = models.ForeignKey('Docs', verbose_name=u'Документ')
    attr = models.ForeignKey(Attribute, verbose_name=u'Наименование атрибута', related_name='Attrname', db_index=True)
    value = models.CharField(u'Значение атрибута', max_length=200)

    def __str__(self):
        return self.doc.abiturient.fullname + ' ' + self.doc.docType.value + ' ' + self.value


# Class that represent document of student
class Docs(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент')
    serialno = models.IntegerField(u'Серия документа', max_length=15, db_index=True, blank=True, null=True)
    number = models.IntegerField(u'Номер документа', max_length=15, db_index=True, blank=True, null=True)
    issueDate = models.DateField(u'Дата выдачи', blank=True, null=True)
    isCopy = models.BooleanField(u'Оригинал документа', default=False)
    docType = models.ForeignKey('AttrValue', verbose_name=u'Тип документа',
                                limit_choices_to={'attribute__name': u'Тип документа'}, related_name='DocType_docs',
                                db_index=True)
    docIssuer = models.ForeignKey('AttrValue', verbose_name=u'Орган выдавший документ',
                                  limit_choices_to={'attribute__name': u'Орган выдавший документ'},
                                  related_name='DocIssuer')

    def __str__(self):
        return self.abiturient.fullname + ' ' + self.docType.value


class DocImages(models.Model):
	doc = models.ForeignKey('Docs', verbose_name='Документ', db_index=True)
	image = models.ImageField(upload_to=DocImagePath)
	def __str__(self):
		return self.doc.abiturient.fullname + ' ' + self.doc.docType.value


class Exams(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент', db_index=True)
    exam_examType = models.ForeignKey('AttrValue', verbose_name=u'Тип экзамена',
                                      limit_choices_to={'attribute__name': u'Тип экзамена'}, related_name='ExamType')
    exam_subjects = models.ForeignKey('AttrValue', verbose_name=u'Дисциплина',
                                      limit_choices_to={'attribute__name': u'Дисциплина'}, related_name='Exam_Subjects')
    points = models.IntegerField(u'Кол-во баллов', max_length=3, blank=True, null=True, db_index=True)
    year = models.IntegerField(u'Год', max_length=4)
    special = models.BooleanField(u'Особые условия', default=False)

    def __str__(self):
        return self.exam_subjects.value + ' ' + str(self.points) + ' ' + str(self.year)


"""
class Department(models.Model):
	university = models.ForeignKey('University')
	name=models.CharField(u'Институт/факультет', max_length=100)
	def __str__(self):
		return self.name

class University(models.Model):
	name=models.CharField(u'Университет', max_length=100)
	def __str__(self):
		return self.name

"""


class EduOrg(models.Model):
    name = models.CharField(u'Образовательное учреждение', max_length=100, db_index=True)
    head = models.ForeignKey('self', null=True, blank=True, db_index=True)
    orgtype = models.ForeignKey('AttrValue', verbose_name=u'Тип образовательного учреждения', null=True, blank=True,
                                db_index=True)

    def __str__(self):
        return self.name


class Education_Prog(models.Model):
    eduorg = models.ForeignKey(EduOrg, verbose_name=u'Образовательное учреждение', db_index=True)
    qualification = models.ForeignKey('AttrValue', verbose_name=u'Квалификация',
                                      limit_choices_to={'attribute__name': u'Квалификация'},
                                      related_name='qualification', db_index=True)
    duration = models.ForeignKey('AttrValue', verbose_name=u'Срок обучения',
                                 limit_choices_to={'attribute__name': u'Срок обучения'}, related_name='duration	',
                                 null=True, blank=True)
    name = models.CharField(u'Направление/специальность', max_length=200, db_index=True)

    def __str__(self):
        return self.name + " " + self.qualification.value


class Template(models.Model):
    name = models.CharField(u'Шаблон', max_length=200, db_index=True)
    org = models.ForeignKey('EduOrg', verbose_name=u'Обр. учреждение', db_index=True)
    active = models.BooleanField(u'Активно', default=True, blank=True)
    type = models.ForeignKey('AttrValue', verbose_name=u'Тип шаблона',
                             limit_choices_to={'attribute__name': u'Тип шаблона'}, db_index=True)

    def __str__(self):
        return self.name


class TemplateAttrs(models.Model):
    template = models.ForeignKey('Template', verbose_name=u'Обр. учреждение', db_index=True)
    attribute = models.ForeignKey('Attribute', verbose_name=u'Атрибут', db_index=True)

    def __str__(self):
        return self.template.name + ' ' + self.attribute.name


class Profile(models.Model):
    edu_prog = models.ForeignKey('Education_Prog')
    name = models.CharField(u'Профиль', max_length=100, db_index=True)

    def __str__(self):
        return self.name + ' ' + self.edu_prog.qualification.value


class ProfileAttrs(models.Model):
    profile = models.ForeignKey('Profile', db_index=True)
    freespaces = models.IntegerField(u'КЦП')
    eduform = models.CharField(u'Форма обучения', choices=EduForm, default='О', max_length=10, null=True, blank=True)
    year = models.IntegerField(u'Год')
    startDate = models.DateField(u'Дата начала приемной кампании')
    endDate = models.DateField(u'Дата конца приемной кампании')

    def __str__(self):
        return self.profile.name + ' ' + self.profile.edu_prog.qualification.value + ' ' + self.eduform


class ApplicationProfiles(models.Model):
    application = models.ForeignKey(Application, verbose_name=u'Заявление', db_index=True)
    profile = models.ForeignKey(ProfileAttrs, verbose_name=u'Профиль направления')
    points = models.IntegerField(u'Кол-во баллов')

    def __str__(self):
        return self.application.abiturient.fullname + ' ' + self.profile.profile.name


class NeedDocuments(models.Model):
    docType = models.ForeignKey('AttrValue', verbose_name=u'Тип документа',
                                limit_choices_to={'attribute__name': u'Тип документа'}, related_name='DocType_need')
    profile = models.ForeignKey('Profile', verbose_name=u'Профиль', db_index=True)


class Exams_needed(models.Model):
    profile = models.ForeignKey('Profile', verbose_name=u'Профиль', db_index=True)
    subject = models.ForeignKey('AttrValue', verbose_name=u'Дисциплина',
                                limit_choices_to={'attribute__name': u'Дисциплина'}, related_name='Subject')
    min_points = models.IntegerField(u'Мин-ое кол-во баллов')

    def __str__(self):
        return self.profile.name + ' ' + self.subject.value + ' ' + str(self.min_points)


class Privilegies(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент', db_index=True)
    category = models.ForeignKey('AttrValue', verbose_name=u'Категория',
                                 limit_choices_to={'attribute__name': u'Категория'}, related_name='Category')
    priv_type = models.ForeignKey('AttrValue', verbose_name=u'Тип привелегии',
                                  limit_choices_to={'attribute__name': u'Тип привелегии'}, related_name='Priv_type')


class Milit(models.Model):
    abiturient = models.OneToOneField('Abiturient', verbose_name=u'Абитуриент', on_delete=models.CASCADE,
                                      primary_key=True)
    liableForMilit = models.BooleanField(u'Военнообязанный', default=False)
    isServed = models.BooleanField(u'служил в армии', default=False, blank=True)
    yearDismissial = models.IntegerField(u'Год увольнения из рядов РА', max_length=4, blank=True, null=True)
    rank = models.ForeignKey(AttrValue, verbose_name=u'Воинское звание', blank=True, null=True, related_name='Rank')


class DepAchieves(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=u'Профиль', db_index=True)
    contest = models.ForeignKey(AttrValue, verbose_name=u'Мероприятие',
                                limit_choices_to={'attribute__name': u'Мероприятие'}, db_index=True,
                                related_name='contest_dep')
    result = models.ForeignKey(AttrValue, verbose_name=u'Достигнутый результат',
                               limit_choices_to={'attribute__name': u'Достигнутый результат'}, db_index=True,
                               related_name='contest_result_dep')
    points = models.IntegerField(u'Баллы')


class Achievements(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name=u'Абитуриент', db_index=True)
    contest = models.ForeignKey('AttrValue', verbose_name=u'Мероприятие',
                                limit_choices_to={'attribute__name': u'Мероприятие'},
                                related_name='contest_achievement')
    result = models.ForeignKey('AttrValue', verbose_name=u'Достигнутый результат',
                               limit_choices_to={'attribute__name': u'Достигнутый результат'},
                               related_name='contest_result_achievement')
