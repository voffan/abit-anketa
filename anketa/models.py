from django.db import models
from django.contrib.auth.models import User
from kladr.models import Street

Sex = (
    (u'М',u'Мужской'),
    (u'Ж',u'Женский'),
    )
Eduform = (
    (u'О',u'Очное'),
    (u'З',u'Заочное')
    )

class Relation(models.Model):
    person=models.ForeignKey('Person',verbose_name=u'RelationPerson')
    abiturient=models.ForeignKey('Abiturient',verbose_name=u'Abiturient')
    relType = models.ForeignKey('AttrValue',verbose_name=u'RelType')

class User(User):
    token = models.CharField(u'Token',max_length=100)

class Abiturient(Person):
    bithplace = models.CharField(u'Место рождения', max_length=100)
    hostel = models.BooleanField(u'Требуется общежитие',default=False)
    nationality = models.ForeignKey(AttrValue,verbose_name=u'Национальность(по желанию)', limit_choices_to={'type__name':u'Национальность'}, db_index = True, blank = True, null = True, related_name='Nationality')
    citizenship = models.ForeignKey(AttrValue,verbose_name=u'Гражданство', db_index = True,related_name='Citizenship')
    foreign_lang = models.ForeignKey('AttrValue', verbose_name=u'Изучаемый иностранный язык',related_name='Foreign')
    milit = models.ForeignKey('Milit', verbose_name=u'Военная обязанность')
    privilegy = models.ForeignKey('Privilegies', verbose_name=u'Привелегия')
    
class AttrType(models.Model):
    name=models.CharField(u"", max_length=100)
    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=250)
    type = models.ForeignKey(AttrType,verbose_name = u'Тип атрибута')
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

class Application(models.Model):
    Department = models.ForeignKey('Department', verbose_name = u'Институт/факультет')
    person = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент')
    date = models.DateField(u'Дата подачи')
    number = models.IntegerField(u'Номер зааявления', max_length=10)
    eduform = models.CharField(u'Форма обучения',choices=Eduform, default='О', max_length=10)
    budget = models.BooleanField(u'В рамках контрольных цифр приёма', default=False)
    withfee = models.BinaryField(u'по договорам об оказании платных обр. услуг', default=False)
    profile = models.ForeignKey('Profile',verbose_name = u'Профиль')

class Address(models.Model):
    person = models.ForeignKey('Person')
    adrs_type = models.ForeignKey('AttrValue', verbose_name=u'Тип адреса', related_name='Adrs_type')
    zipcode = models.CharField(u'Индекс', max_length=6, null=True, blank=True)
    street = models.ForeignKey('Street',verbose_name=u'Улица', related_name ='Street')
    house = models.CharField(u'дом', max_length=5)
    building = models.CharField(u'корпус', max_length=5, null=True, blank=True)
    flat = models.CharField(u'квартира', max_length=5, null=True, blank=True)
    adrs_type_same = models.BooleanField(u'Адрес по прописке совпадает с адресом фактического проживания', default=False)
    

class Contacts(models.Model):
    person = models.ForeignKey('Person',verbose_name = u'Человек')
    contact = models.ForeignKey('AttrValue',verbose_name=u'Контактная информация')

class DocAttr(models.Model):
    doc = models.ForeignKey('Docs', verbose_name=u'Документ')
    attr = models.ForeignKey(AttrValue, verbose_name = u'Значение атрибута', related_name='Attrname', db_index = True)

class Docs(models.Model):
    abiturient = models.ForeignKey('Abiturient', verbose_name = u'Абитуриент')
    serialno = models.IntegerField(u'Серия документа', max_length=15)
    number = models.IntegerField(u'Номер документа', max_length=15)
    issueDate = models.DateField(u'Дата выдачи')
    isCopy = models.BooleanField(u'Оригинал документа', default=False)
    docType = models.ForeignKey('AttrValue', verbose_name=u'Тип документа', related_name='DocType')
    docIssuer = models.ForeignKey('AttrValue', verbose_name=u'Орган выдавший документ', related_name='DocIssuer')

class Exams(models.Model):
    person = models.ForeignKey('Person')
    exam_examType = models.ForeignKey('AttrValue', verbose_name=u'Тип экзамена', related_name='ExamType')
    exam_subjects = models.ForeignKey('AttrValue', verbose_name=u'Дисциплина',related_name='Exam_Subjects')
    points = models.IntegerField(u'Кол-во баллов', max_length=3, blank = True, null = True)
    year = models.IntegerField(u'Год', max_length=4)

class Department(models.Model):
    university = models.ForeignKey('University')
    name=models.CharField(u'Институт/факультет', max_length=100)

class University(models.Model):
    name=models.CharField(u'Университет', max_length=100)

class Qualification(models.Model):
    name=models.CharField(u'Название', max_length=100)

class Education_Prog(models.Model):
    department = models.ForeignKey(Department)
    qual=models.ForeignKey('Qualification')
    name=models.CharField(u'Направление/специальность', max_length=100)

class Profile(models.Model):
    edu_prog=models.ForeignKey('Education_Prog')
    application=models.ForeignKey('Application')
    needDoc=models.ForeignKey('NeedDocuments')
    name=models.CharField(u'Профиль', max_length=100)
    freespaces=models.IntegerField(u'Места')
    year=models.IntegerField(u'Год')

class NeedDocuments(models.Model)
    docType = models.ForeignKey('AttrValue', verbose_name=u'Тип документа', related_name='DocType')

class Exams_needed(models.Model):
    profile=models.ForeignKey('Profile')
    min_points=models.IntegerField(u'Мин-ое кол-во баллов', max_length=100)
    subject = models.ForeignKey('AttrValue', verbose_name=u'Дисциплина', related_name='Subject')
	

class Privilegies(models.Model):
    person = models.ForeignKey('Person')
    category = models.ForeignKey('AttrValue', verbose_name=u'Категория', related_name='Category')
    priv_type = models.ForeignKey('AttrValue', verbose_name=u'тип', related_name='Priv_type')


class Milit(models.Model):
    person=models.ForeignKey(Person, verbose_name = u'Абитуриент')
    liableForMilit = models.BooleanField(u'Военнообязанный', default=False)
    isServed=models.BooleanField(u'служил в армии', default=False, blank=True)
    yearDismissial=models.IntegerField(u'Год увольнения из рядов РА', max_length=4, blank=True, null= True)
    rank = models.ForeignKey(AttrValue, verbose_name=u'Воинское звание',blank=True, null= True,related_name='Rank')

class DepAchieves(models.Model):
    department = models.ForeignKey(Department, verbose_name = u'Институт/факультет', db_index = True, blank = True, null = True)
    qual = models.ForeignKey(Qualification, verbose_name = u'Квалификация', db_index = True)
    name = models.CharField(u'Наименование', max_length = 200, db_index = True)
    points = models.IntegerField(u'Баллы')

class Achievements(models.Model):
    person = models.ForeignKey(Person, verbose_name = u'Абитуриент', db_index = True)
    achieve = models.ForeignKey(DepAchieves, verbose_name = u'Достижение', db_index = True)
