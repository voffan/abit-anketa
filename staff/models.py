from django.db import models
from anketa.models import Attribute, Department, AttrValue, Application, User

class Employee(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь', db_index=True)
    department = models.ForeignKey(Department,verbose_name=u'Подразделение', db_index=True)
    position = models.ForeignKey('Position', verbose_name=u'Должность',db_index=True)
    uniemployee = models.IntegerField(u'УнивСотрудник', db_index=True)
    fullname = models.CharField(u'ФИО', max_length = 200, db_index=True)
    first_name = models.CharField(u'Фамилия', max_length=100)
    mid_name = models.CharField(u'Имя', max_length = 100)
    last_name = models.CharField(u'Отчество', max_length = 100)
    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        s=''
        if len(self.first_name)>0:
            s+=self.first_name
        if len(self.mid_name)>0:
            s+=' '+self.mid_name
        if len(self.last_name)>0:
            s+=' '+self.last_name
        self.fullname = s
        super(Employee, self).save(*args, **kwargs)

class Position(models.Model):
    name = models.CharField(u'Должность',max_length=200, db_index=True)
    def __str__(self):
        return self.name

class Contacts(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'Сотрудник', db_index=True)
    contact_type = models.ForeignKey(AttrValue, verbose_name=u'Тип контакта')
    value = models.CharField(u'Контакт', max_length = 150, db_index=True)
    def __str__(self):
        return self.employee.fullname+' '+value
        