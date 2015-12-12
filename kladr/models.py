#-*- coding: utf-8 -*-

from django.db import models


class Altnames(models.Model):
    oldcode = models.CharField(u'Старый код',max_length = 19)
    newcode = models.CharField(u'Новый код',max_length = 19)
    level = models.CharField(u'Уровень объекта',max_length = 1)

class Doma(models.Model):
    name = models.CharField(u'Номера домов',max_length = 40, db_index = True)
    korp = models.CharField(u'Корпус дома',max_length = 10, null=True, blank=True, db_index = True)
    socr = models.CharField(u'Сокращенное наименование типа объекта',max_length = 10)
    code = models.CharField(u'Код',max_length = 19, db_index = True)
    index = models.CharField(u'Почтовый индекс',max_length = 6, null=True, blank=True, db_index = True)
    gninmb = models.CharField(u'Код ИФНС',max_length = 4, null=True, blank=True, db_index = True)
    uno = models.CharField(u'Код терр-го участка ИФНС',max_length = 4, null=True, blank=True, db_index = True)
    ocatd = models.CharField(u'ОКАТО',max_length = 11, null=True, blank=True, db_index = True)
    def __unicode__(self):
        return self.name

class Flat(models.Model):
    name = models.CharField(u'Номер квартиры',max_length = 40, db_index = True)
    code = models.CharField(u'Код',max_length = 23, db_index = True)
    index = models.CharField(u'Почтовый индекс',max_length = 6, null=True, blank=True, db_index = True)
    gninmb = models.CharField(u'Код ИФНС(ИМНС)', null=True, blank=True, max_length = 4)
    uno = models.CharField(u'Код терр-го участка ИФНС', null=True, blank=True, max_length = 4)
    np = models.CharField(u'Номер подъезда', null=True, blank=True, max_length = 4)
    def __unicode__(self):
        return self.name

class Kladr(models.Model):
    name = models.CharField(u'Наименование',max_length = 40, db_index = True)
    socr = models.CharField(u'Сокращенное наименование типа объекта',max_length = 10)
    code = models.CharField(u'Код',max_length = 13, db_index = True)
    index = models.CharField(u'Почтовый индекс',max_length = 6, null=True, blank=True, db_index = True)
    gninmb = models.CharField(u'Код ИФНС',max_length = 4, null=True, blank=True, db_index = True)
    uno = models.CharField(u'Код терр-го участка ИФНС',max_length = 4, null=True, blank=True, db_index = True)
    ocatd = models.CharField(u'ОКАТО',max_length = 11, null=True, blank=True, db_index = True)
    status = models.CharField(u'Статус объекта',max_length = 1, db_index = True)
    def __unicode__(self):
        return self.name

class Socrbase(models.Model):
    level = models.CharField(u'Уровень объекта',max_length = 5, db_index = True)
    scname = models.CharField(u'Сокращенное наименование тип объекта',max_length = 10, db_index = True)
    socrname = models.CharField(u'Полное наименование тип объекта',max_length = 29, db_index = True)
    kod_t_st = models.CharField(u'Код типа объекта',max_length = 3, db_index = True)
    def __unicode__(self):
        return self.scname

class Street(models.Model):
    name = models.CharField(u'Наименование',max_length = 40, db_index = True)
    socr = models.CharField(u'Сокращенное наименование тип объекта',max_length = 10)
    code = models.CharField(u'Код',max_length = 17, db_index = True)
    index = models.CharField(u'Почтовый индекс',max_length = 6, null=True, blank=True, db_index = True)
    gninmb = models.CharField(u'Код ИФНС',max_length = 4, null=True, blank=True, db_index = True)
    uno = models.CharField(u'Код терр-го участка ИФНС',max_length = 4, null=True, blank=True, db_index = True)
    ocatd = models.CharField(u'ОКАТО',max_length = 11, null=True, blank=True, db_index = True)
    def __unicode__(self):
        return self.name