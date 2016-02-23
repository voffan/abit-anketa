from django.db import models
from django.contrib.auth.models import User
##from kladr.models import Street

Sex = (
    (u'М',u'Мужской'),
    (u'Ж',u'Женский'),
    )
Eduform = (
    (u'О',u'Очное'),
    (u'З',u'Заочное')
    )

class Relation(models.Model):
    person=models.ForeignKey('Person',verbose_name=u'Родственник') # ??????
    abiturient=models.ForeignKey('Abiturient',verbose_name=u'Абитуриент', db_index=True)# ??????# ??????# ??????# ??????# ??????# ??????# ??????# ??????# ??????
    relType = models.ForeignKey('AttrValue',verbose_name=u'Тип связи', db_index=True)

class User(User):
    token = models.CharField(u'Token',max_length=100, db_index = True)
    isEmployee = models.BooleanField(u'Сотрудник')

class AttrType(models.Model):
    name=models.CharField(u"", max_length=100)
    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(u'Наименование атрибута',max_length=250, db_index=True)
    type = models.ForeignKey(AttrType,verbose_name = u'Тип атрибута', db_index=True)
    def __str__(self):
        return self.name

class AttrValue(models.Model):
    value = models.CharField(u'Значение', max_length=250, db_index = True)
    parent = models.ForeignKey('self', null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=u'Атрибут', db_index = True)
    def __str__(self):
        return self.attribute.name+' '+self.value

class Person(models.Model):
    lname = models.CharField(u'Фамилия', max_length=30)
    nname = models.CharField(u'Имя', max_length=30)
    mname = models.CharField(u'Отчество', max_length=30)
    sex = models.CharField(u'Пол', choices=Sex, max_length=1, default='М')
    birthdate = models.DateField(u'Дата рождения')

class Abiturient(Person):
    bithplace = models.CharField(u'Место рождения', max_length=100)
    hostel = models.BooleanField(u'Требуется общежитие',default=False)
    nationality = models.ForeignKey(AttrValue,verbose_name=u'Национальность(по желанию)', limit_choices_to={'type__name':u'Национальность'}, db_index = True, blank = True, null = True, related_name='Nationality')
    citizenship = models.ForeignKey(AttrValue,verbose_name=u'Гражданство', db_index = True,related_name='Citizenship')
    foreign_lang = models.ForeignKey('AttrValue', verbose_name=u'Изучаемый иностранный язык',related_name='Foreign')

class Application(models.Model):
    department = models.ForeignKey('Department', verbose_name = u'Институт/факультет', db_index=True)
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент', db_index=True)
    date = models.DateField(u'Дата подачи', db_index=True)
    number = models.IntegerField(u'Номер зааявления', max_length=10)
    eduform = models.CharField(u'Форма обучения',choices=Eduform, default='О', max_length=10)
    budget = models.BooleanField(u'В рамках контрольных цифр приёма', default=False)
    withfee = models.BooleanField(u'по договорам об оказании платных обр. услуг', default=False)
    profile = models.ForeignKey('Profile',verbose_name = u'Профиль')
    appState = models.ForeignKey('AttrValue',verbose_name=u'Состояние заявления', db_index=True)
    points = models.IntegerField(u'Кол-во баллов', db_index=True)

class Address(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент')
    adrs_type = models.ForeignKey('AttrValue', verbose_name=u'Тип адреса', related_name='Adrs_type')
    zipcode = models.CharField(u'Индекс', max_length=6, null=True, blank=True)
    street = models.ForeignKey('Street',verbose_name=u'Улица', related_name ='Street')
    house = models.CharField(u'дом', max_length=5)
    building = models.CharField(u'корпус', max_length=5, null=True, blank=True)
    flat = models.CharField(u'квартира', max_length=5, null=True, blank=True)
    adrs_type_same = models.BooleanField(u'Адрес по прописке совпадает с адресом фактического проживания', default=False)

class Contacts(models.Model):
    person = models.ForeignKey('Person',verbose_name = u'Человек', db_index=True)
    contact_type = models.ForeignKey('AttrValue',verbose_name=u'Тип контакта', related_name="ContactTypeAnketa")
    value = models.CharField(u'Контакт', max_length=200)

class DocAttr(models.Model):
    doc = models.ForeignKey('Docs', verbose_name=u'Документ')
    attr = models.ForeignKey(AttrValue, verbose_name = u'Наименование атрибута', related_name='Attrname', db_index = True)
    value = models.CharField(u'Значение атрибута', max_length=200)

class Docs(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент')
    serialno = models.IntegerField(u'Серия документа', max_length=15, db_index=True, blank=True, null=True)
    number = models.IntegerField(u'Номер документа', max_length=15, db_index=True, blank=True, null=True)
    issueDate = models.DateField(u'Дата выдачи', blank=True, null=True)
    isCopy = models.BooleanField(u'Оригинал документа', default=False)
    docType = models.ForeignKey('AttrValue', verbose_name=u'Тип документа', related_name='DocType_docs', db_index=True)
    docIssuer = models.ForeignKey('AttrValue', verbose_name=u'Орган выдавший документ', related_name='DocIssuer')

class Exams(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент', db_index=True)
    exam_examType = models.ForeignKey('AttrValue', verbose_name=u'Тип экзамена', related_name='ExamType')
    exam_subjects = models.ForeignKey('AttrValue', verbose_name=u'Дисциплина',related_name='Exam_Subjects')
    points = models.IntegerField(u'Кол-во баллов', max_length=3, blank = True, null = True, db_index=True)
    year = models.IntegerField(u'Год', max_length=4)

class Department(models.Model):
    university = models.ForeignKey('University')
    name=models.CharField(u'Институт/факультет', max_length=100)

class University(models.Model):
    name=models.CharField(u'Университет', max_length=100)
    def __str__(self):
        return self.name

class Education_Prog(models.Model):
    department = models.ForeignKey(Department, verbose_name=u'УЧП', db_index=True)
    qualification=models.ForeignKey('AttrValue', verbose_name=u'Квалификация', db_index=True)
    name=models.CharField(u'Направление/специальность', max_length=200, db_index=True)

class Profile(models.Model):
    edu_prog=models.ForeignKey('Education_Prog')
    name=models.CharField(u'Профиль', max_length=100, db_index=True)
    freespaces=models.IntegerField(u'Места')
    year=models.IntegerField(u'Год')

class NeedDocuments(models.Model):
    docType = models.ForeignKey('AttrValue', verbose_name=u'Тип документа', related_name='DocType_need')
    profile = models.ForeignKey('Profile', verbose_name=u'Профиль', db_index=True)

class Exams_needed(models.Model):
    profile=models.ForeignKey('Profile', verbose_name=u'Профиль', db_index=True)
    subject = models.ForeignKey('AttrValue', verbose_name=u'Дисциплина', related_name='Subject')
    min_points=models.IntegerField(u'Мин-ое кол-во баллов')

class Privilegies(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент')
    category = models.ForeignKey('AttrValue', verbose_name=u'Категория', related_name='Category')
    priv_type = models.ForeignKey('AttrValue', verbose_name=u'тип', related_name='Priv_type')

class Milit(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент')
    liableForMilit = models.BooleanField(u'Военнообязанный', default=False)
    isServed=models.BooleanField(u'служил в армии', default=False, blank=True)
    yearDismissial=models.IntegerField(u'Год увольнения из рядов РА', max_length=4, blank=True, null= True)
    rank = models.ForeignKey(AttrValue, verbose_name=u'Воинское звание',blank=True, null= True,related_name='Rank')

class DepAchieves(models.Model):
    profile = models.ForeignKey(Profile, verbose_name = u'Профиль', db_index = True)
    contest = models.ForeignKey(AttrValue, verbose_name = u'Мероприятие', db_index = True, related_name='contest_dep')
    result = models.ForeignKey(AttrValue, verbose_name = u'Достигнутый результат', db_index = True, related_name='contest_result_dep')
    points = models.IntegerField(u'Баллы')

class Achievements(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент', db_index=True)
    contest = models.ForeignKey(AttrValue, verbose_name = u'Мероприятие', db_index = True, related_name='contest_ach')
    result = models.ForeignKey(AttrValue, verbose_name = u'Достигнутый результат', db_index = True, related_name='contest_result_ach')
