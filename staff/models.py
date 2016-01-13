from django.db import models
from django.contrib.auth.models import User
from anketa.models import Attribute, Department, AttrValue

class Employee(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь', db_index=True)
    department = models.ForeignKey(Department,verbose_name=u'Подразделение', db_index=True)
    position = models.ForeignKey('Position', verbose_name=u'Должность')
    uniemployee = models.IntegerField(u'УнивСотрудник', db_index=True)
    fullname = models.CharField(u'ФИО', max_length = 300, db_index=True)
    first_name = models.Charfield(u'Фамилия', max_length=100)
    mid_name = models.Charfield(u'Имя', max_length = 100)
    last_name = models.Charfield(u'Отчество', max_length = 100)
    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        s=''
        if len(self.firstname)>0:
            s+=self.firstname
        if len(self.name)>0:
            s+=' '+self.name
        if len(self.midname)>0:
            s+=' '+self.midname
        self.fullname = s
        super(Person, self).save(*args, **kwargs)

class Position(models.Model):
    name = models.Charfield(u'Должность',max_length=200, db_index=True)
    def __str__(self):
        return self.name

class Contacts(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'Сотрудник', db_index=True)
    contact_type = models.ForeignKey(Attribute, verbose_name=u'Тип контакта')
    value = models.CharField(u'Контакт', max_length = 150, db_index=True)
    def __str__(self):
        return self.employee.fullname+' '+value