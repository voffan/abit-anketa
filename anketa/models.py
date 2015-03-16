from django.db import models

class Person(models.Model):
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    name = models.CharField(max_length=30, verbose_name="Имя")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество")
    sex = models.CharField(choices=((u'М',u'Мужской'),(u'Ж',u'Женский')), max_length=1, verbose_name="Пол")
    born_date = models.DateField(verbose_name="Дата рождения")
    id_doc = models.ForeignKey('Universal_directory', verbose_name="вид", related_name='id_doc')
    doc_serial = models.CharField(max_length=10, verbose_name="серия")
    doc_no = models.CharField(max_length=30, verbose_name="номер")
    doc_distributed_date = models.DateField(verbose_name="дата выдачи")
    doc_distributed_organisation = models.CharField(max_length=100, verbose_name="кем выдан")
    is_checked = models.BooleanField(default=False, verbose_name="Проверен")
    to_delete = models.BooleanField(default=False, verbose_name="На удаление")
    prev_edu_level = models.ForeignKey('Universal_directory', verbose_name="Предыд. образ-ние", related_name='prev_edu_level')
    prev_edu_start = models.DateField(verbose_name="Дата поступления")
    prev_edu_end = models.DateField(verbose_name="дата окончания")
    prev_edu_organisation = models.ForeignKey('Universal_directory', verbose_name="учебное заведение", related_name='prev_edu_organisation')
    prev_edu_doc_type = models.ForeignKey('Universal_directory', verbose_name="вид документа об образовании", related_name='prev_edu_doc_type')
    prev_edu_doc_seria = models.CharField(max_length=10, verbose_name="серия")
    prev_edu_doc_num = models.CharField(max_length=30, verbose_name="номер")
    hotel = models.BooleanField(default=False, verbose_name="Требуется общежитие")
    foreign_lang = models.ForeignKey('Universal_directory', verbose_name="Изучаемый иностранный язык", related_name='foreign_lang')

class Application(models.Model):
    id_person = models.ForeignKey('Person')
    id_pln = models.ForeignKey('Edu_prog')
    reg_no = models.CharField(max_length=30, verbose_name="шифр по журналу")
    date_in = models.DateField(verbose_name="дата")
    is_confirmed = models.BooleanField(default=False, verbose_name="Подтверждено")
    to_delete = models.BooleanField(default=False, verbose_name="На удаление")
    to_export = models.BooleanField(default=False, verbose_name="На экспорт")
    prev_edu_doc_orig = models.BooleanField(default=False, verbose_name="Оригинал документа об образовании")
    is_exported = models.BooleanField(default=False, verbose_name="Экспортировано")

class Address(models.Model):
    id_person = models.ForeignKey('Person')
    id_addr_type = models.ForeignKey('Universal_directory', verbose_name="Тип адреса", related_name='id_addr_type')
    id_adm_territory = models.ForeignKey('Universal_directory', verbose_name="область\край\респ.", related_name='id_adm_territory', null=True, blank=True)
    id_adm_unit = models.ForeignKey('Universal_directory', verbose_name="Район\улус", related_name='id_adm_unit', null=True, blank=True)
    id_settlement = models.ForeignKey('Universal_directory', verbose_name="Город\село", related_name='id_settlement')
    post_index = models.CharField(max_length=6, verbose_name="Индекс", null=True, blank=True)
    street_name = models.CharField(max_length=151, verbose_name="Улица\проспект")
    house_no = models.CharField(max_length=5, verbose_name="дом")
    block_no = models.CharField(max_length=5, verbose_name="корпус", null=True, blank=True)
    apart_no = models.CharField(max_length=5, verbose_name="квартира", null=True, blank=True)

class EGE(models.Model):
    id_person = models.ForeignKey('Person')
    id_subject = models.ForeignKey('Universal_directory', verbose_name="предмет", related_name='id_subject')
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="год")
    mark = models.DecimalField(max_digits=3, decimal_places=0, verbose_name="оценка")
    sert_no = models.CharField(max_length=15, verbose_name="номер свидетельства")
    is_checked = models.BooleanField(default=False, verbose_name="Проверен")

class Edu_prog(models.Model):
    id_spec = models.ForeignKey('Universal_directory', verbose_name="Специализация", related_name='id_spec')
    id_specialn = models.ForeignKey('Universal_directory', verbose_name="Специальность", related_name='id_specialn')
    id_study_form = models.ForeignKey('Universal_directory', verbose_name="Форма обучения", related_name='id_study_form')
    id_institute = models.ForeignKey('Universal_directory', verbose_name="Институт", related_name='id_institute')

class Privilegies(models.Model):
    id_person = models.ForeignKey('Person')
    id_privilege = models.ForeignKey('Universal_directory', verbose_name="Льгота\приоритет")

class Milit(models.Model):
    id_person = models.ForeignKey('Person', primary_key=True)
    served = models.BooleanField(default=False, verbose_name="служил в армии")
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="год увольнения из рядов РА", null=True, blank=True)
    rank = models.CharField(max_length=50, verbose_name="Воинское звание", null=True, blank=True)

class Edu_prog_need_exams(models.Model):
    id_pln = models.ForeignKey('Edu_prog')
    id_subject = models.ForeignKey('Universal_directory')
    min_mark = models.SmallIntegerField()

class Need_exams(models.Model):
    id_person = models.ForeignKey('Person')
    subj = models.ForeignKey('Universal_directory', related_name='subj', verbose_name="Дисциплина")
    exam_form = models.ForeignKey('Universal_directory', related_name='exam_form', verbose_name="Форма экзамена")

class Universal_directory(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey('self', null=True, blank=True)
    type = models.ForeignKey('Directory_types')
    def __unicode__(self):
        return self.name

class Directory_types(models.Model):
    name = models.CharField(max_length=250)

class Feedback(models.Model):
    email = models.EmailField(verbose_name=u'Ваш email для нашего ответа (не обязателен)', null=True, blank=True)
    text = models.TextField(verbose_name=u'Сообщение')
