from django.db import models
from django.contrib.auth.models import User
from anketa.models import Attribute, Department, AttrValue


class Employee(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь', db_index=True)
    department = models.ForeignKey(Department,verbose_name=u'Подразделение')
    #position = models.ForeignKey(UniEmployees, verbose_name=u'Должность')
    position = models.ForeignKey('Position', verbose_name=u'Должность')
    ufirst_name = models.ForeignKey('UniEmployees', verbose_name=u'Фамилия', db_index=True)
    ulast_name = models.ForeignKey('UniEmployees', verbose_name=u'Имя', db_index=True)
    umiddle_name = models.ForeignKey('UniEmployees', verbose_name=u'Отчество', db_index=True)
    fullname = models.CharField(u'ФИО', max_length = 300, db_index=True)
    def __unicode__(self):
        return self.fullname

class EmplContacts(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'ФИО')
    #contact_type = models.ForeignKey(Attribute, verbose_name=u'Тип контакта')
    #value = models.CharField(u'Контакт', max_length = 150, db_index=True)
    value = models.ForeignKey(AttrValue, verbose_name=u'Значение', db_index=True)

class Position(models.Model):
    name = models.Charfield(u'Должность',max_length=200, db_index=True)


class UniEmployees(models.Model):
    first_name = models.Charfield(u'Фамилия', max_length=100, db_index=True)
    last_name = models.Charfield(u'Имя', max_length = 100, db_index=True)
    middle_name = models.Charfield(u'Отчество', max_length = 100, db_index = True)
    #position = models.Charfield(u'Должность', max_length =200)

class News(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'Автор')
    NewsName = models.CharField(u'Название новости', max_length=30)
    Description = models.CharField(u'Описание', max_length=100)
    NewsDate = models.DateField(u'Дата новости', db_index=True)
    NewsText = models.CharField(u'Контент', max_length=700)
