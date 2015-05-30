from django.db import models
from django.contrib.auth.models import User
from anketa.models import Attribute, Department, AttrValue
from time import strftime, gmtime
import os

def imagepath(instance, filename):
    return os.path.join('news',strftime('%d%m%Y',gmtime()),str(instance.news.id),filename)

class Employee(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь', db_index=True)
    department = models.ForeignKey(Department,verbose_name=u'Подразделение')
    first_name = models.CharField(u'Фамилия', max_length=100, db_index=True)
    last_name = models.CharField(u'Имя', max_length=100, db_index=True)
    middle_name = models.CharField(u'Отчество', max_length=100, db_index=True)
    fullname = models.CharField(u'ФИО', max_length = 300, db_index=True)
    position = models.CharField(u'Должность', max_length=200)
    
    def __str__(self):
        return self.fullname

class EmplContacts(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'Сотрудник', db_index=True)
    contact_type = models.ForeignKey(AttrValue, verbose_name=u'Тип контакта')
    value = models.CharField(u'Контакт', max_length = 150, db_index=True)
    
    def __str__(self):
        return self.employee.fullname+' '+value

class News(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'Автор')
    NewsName = models.CharField(u'Название новости', max_length=30)
    Description = models.CharField(u'Описание', max_length=100)
    NewsDate = models.DateField(u'Дата новости', db_index=True)
    NewsText = models.TextField(u'Контент')
    
    def __str__(self):
        return self.NewsName

    
class Img(models.Model):
    news = models.ForeignKey(News, verbose_name=u'Название новости')
    img  = models.ImageField(upload_to= imagepath, verbose_name=u'Имя', help_text='150x150px')
    def __str__(self):
        return self.news.NewsName+'_1'
