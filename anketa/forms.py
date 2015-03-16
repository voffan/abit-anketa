from django.forms import Form, ModelForm, CharField, DateField, Select, ModelChoiceField, BooleanField, ChoiceField, DecimalField
from anketa.models import Person, Application, Address, Universal_directory, Directory_types, Milit, EGE, Privilegies, Need_exams
from django.forms.widgets import NumberInput, Select, TextInput, RadioSelect
from django.forms.extras.widgets import SelectDateWidget

class Person_form(ModelForm):
    born_date = DateField(label=u'Дата рождения',widget=SelectDateWidget(years=range(2000,1900,-1)))
    doc_distributed_date = DateField(label=u'Дата выдачи',widget=SelectDateWidget(years=range(2014,1900,-1)))
    prev_edu_start = DateField(label=u'Дата поступления',widget=SelectDateWidget(years=range(2014,1900,-1)))
    prev_edu_end = DateField(label=u'Дата окончания',widget=SelectDateWidget(years=range(2014,1900,-1)))
    id_doc = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Документ')), label=u'Вид')
    prev_edu_level = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Образование')), label=u'Предыд. образ-ние')
    prev_edu_organisation = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Учебное заведение')), label=u'Учебное заведение', required=False)
    prev_edu_organisation_name = CharField(label=u'Учебное заведение', required=False)
    prev_edu_doc_type = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Документ об образовании')), label=u'Вид')
    hotel = BooleanField(label=u'Требуется общежитие', required=False)
    foreign_lang = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Иностранный язык')), label=u'Изучаемый иностранный язык')
    def clean(self):
        cleaned_data = super(Person_form, self).clean()
        prev_edu_organisation = cleaned_data.get('prev_edu_organisation')
        prev_edu_organisation_name = cleaned_data.get('prev_edu_organisation_name')
        if not prev_edu_organisation and not prev_edu_organisation_name:
            msg = u'Обязательное поле'
            self._errors['prev_edu_organisation'] = self.error_class([msg])
            self._errors['prev_edu_organisation_name'] = self.error_class([msg])
            del cleaned_data['prev_edu_organisation']
            del cleaned_data['prev_edu_organisation_name']
        if not prev_edu_organisation and prev_edu_organisation_name:
            if 0 == Universal_directory.objects.filter(name=prev_edu_organisation_name,type=Directory_types.objects.get(name=u'Учебное заведение')).count():
                if 0 == Universal_directory.objects.filter(name=prev_edu_organisation_name,type=Directory_types.objects.get(name=u'Учебное заведение (пользовательский ввод)')).count():
                    Universal_directory(name=prev_edu_organisation_name,type=Directory_types.objects.get(name=u'Учебное заведение (пользовательский ввод)')).save()
                cleaned_data['prev_edu_organisation'] = Universal_directory.objects.get(name=prev_edu_organisation_name,type=Directory_types.objects.get(name=u'Учебное заведение (пользовательский ввод)'))
            else:
                cleaned_data['prev_edu_organisation'] = Universal_directory.objects.get(name=prev_edu_organisation_name,type=Directory_types.objects.get(name=u'Учебное заведение'))
        return cleaned_data
    class Meta:
        model = Person
        fields = ('surname', 'name', 'patronymic', 'sex', 'born_date', 'id_doc', 'doc_serial', 'doc_no', 'doc_distributed_date', 'doc_distributed_organisation', 'prev_edu_level', 'prev_edu_start', 'prev_edu_end', 'prev_edu_organisation', 'prev_edu_organisation_name', 'prev_edu_doc_type', 'prev_edu_doc_seria', 'prev_edu_doc_num', 'hotel', 'foreign_lang')

class Application_form(ModelForm):
    id_institute = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Факультет / институт')), label=u'Факультет / институт', empty_label=None)
    id_specialn = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Специальность')), label=u'Направление (специальность)')
    id_spec = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Специализация')), label=u'Профиль (специализация)')
    id_study_form = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Форма обучения')), label=u'Форма обучения', empty_label=None)
    def __init__(self, *args, **kwargs):
        super(Application_form, self).__init__(*args, **kwargs)
        if 0 == len(self.data):
            self.fields['id_spec'].queryset = Universal_directory.objects.none()
    class Meta:
        model = Application
        fields = []

class Address_form(ModelForm):
    id_adm_territory = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Субъект федерации')), label=u'область\край\респ.')
    id_adm_unit = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Муниципальный район')), label=u'Район\улус', required=False)
    adm_unit_name = CharField(label='Район\улус', required=False)
    id_settlement = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Населённый пункт')), label=u'Город\село', required=False)
    settlement_name = CharField(label='Город\село', required=False)
    post_index = CharField(label='Индекс', required=False)
    block_no = CharField(label='Корпус', required=False)
    apart_no = CharField(label='Квартира', required=False)
    def __init__(self, *args, **kwargs):
        super(Address_form, self).__init__(*args, **kwargs)
        if 0 == len(self.data):
            self.fields['id_adm_unit'].queryset = Universal_directory.objects.none()
            self.fields['id_settlement'].queryset = Universal_directory.objects.filter(parent=None,type=Directory_types.objects.get(name=u'Населённый пункт'))
    def clean(self):
        cleaned_data = super(Address_form, self).clean()
        id_adm_unit = cleaned_data.get('id_adm_unit')
        adm_unit_name = cleaned_data.get('adm_unit_name')
        id_settlement = cleaned_data.get('id_settlement')
        settlement_name = cleaned_data.get('settlement_name')
        if not id_settlement and not settlement_name:
            msg = u'Обязательное поле'
            self._errors['id_settlement'] = self.error_class([msg])
            self._errors['settlement_name'] = self.error_class([msg])
            del cleaned_data['id_settlement']
            del cleaned_data['settlement_name']
        if not id_adm_unit and adm_unit_name:
            if 0 == Universal_directory.objects.filter(name=cleaned_data['adm_unit_name'],type=Directory_types.objects.get(name=u'Муниципальный район (пользовательский ввод)')).count():
                Universal_directory(name=cleaned_data['adm_unit_name'],type=Directory_types.objects.get(name=u'Муниципальный район (пользовательский ввод)')).save()
            cleaned_data['id_adm_unit'] = Universal_directory.objects.get(name=cleaned_data['adm_unit_name'],type=Directory_types.objects.get(name=u'Муниципальный район (пользовательский ввод)'))
        if not id_settlement and settlement_name:
            if 0 == Universal_directory.objects.filter(name=cleaned_data['settlement_name'],type=Directory_types.objects.get(name=u'Населённый пункт (пользовательский ввод)')).count():
                Universal_directory(name=cleaned_data['settlement_name'],type=Directory_types.objects.get(name=u'Населённый пункт (пользовательский ввод)')).save()
            cleaned_data['id_settlement'] = Universal_directory.objects.get(name=cleaned_data['settlement_name'],type=Directory_types.objects.get(name=u'Населённый пункт (пользовательский ввод)'))
        return cleaned_data
    class Meta:
        model = Address
        fields = ('id_adm_territory', 'id_adm_unit', 'adm_unit_name', 'id_settlement', 'settlement_name', 'post_index', 'street_name', 'house_no', 'block_no', 'apart_no')

class Address_coincides_form(Form):
    is_coincides = ChoiceField(choices=((u'',u'---------'),(u'true',u'да'),(u'false',u'нет')),label=u'Совпадает с адресом абитуриента по прописке')

class EGE_form(ModelForm):
    id_subject = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Дисциплина')), label=u'Дисциплина')
    year = DecimalField(max_digits=4, decimal_places=0, widget=Select(choices=((u'',u'---'),('2014','2014'),('2013','2013'),('2012','2012'),('2011','2011'))))
    mark = DecimalField(max_digits=3, decimal_places=0, widget=NumberInput(attrs={'min': '0', 'max': '100', 'step': '1'}))
    class Meta:
        model = EGE
        fields = ('id_subject', 'sert_no', 'year', 'mark')

class Milit_form(ModelForm):
    served = BooleanField(widget=Select(choices=((u'',u'---------'),(u'true',u'да'),(u'false',u'нет'))), label=u'Служил в армии', required=False)
    year = DecimalField(max_digits=4, decimal_places=0, widget=NumberInput(attrs={'min': '1990', 'max': '2014', 'step': '1'}), label=u'год увольнения из рядов РА', required=False)
    def clean(self):
        cleaned_data = super(Milit_form, self).clean()
        served = cleaned_data.get('served')
        year = cleaned_data.get('year')
        rank = cleaned_data.get('rank')
        msg = u'Обязательное поле'
        if '' == served:
            self._errors['served'] = self.error_class([msg])
            del cleaned_data['served']
        if served:
            if not year:
                self._errors['year'] = self.error_class([msg])
                del cleaned_data['year']
            if not rank:
                self._errors['rank'] = self.error_class([msg])
                del cleaned_data['rank']
        return cleaned_data
    class Meta:
        model = Milit
        fields = ('served', 'year', 'rank')

class Is_mil_service_form(Form):
    is_mil_service = ChoiceField(choices=((u'',u'---------'),(u'false',u'невоеннообязанный'),(u'true',u'военнообязанный')),label=u'Военная обязанность')

class Privilegies_form(ModelForm):
    id_privilege = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Льготы и приоритеты')), label=u'Льгота\приоритет')
    class Meta:
        model = Privilegies
        fields = ('id_privilege',)

class Need_exams_form(ModelForm):
    subj = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Дисциплина')), label=u'Дисциплина')
    exam_form = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Форма экзамена')), label=u'Форма экзамена')
    class Meta:
        model = Need_exams
        fields = ('subj', 'exam_form')


class Step_Name(Form):
    surname = CharField(
        label=u"Фамилия", 
        max_length=30, 
        widget=TextInput({ "placeholder": "Сидоров" }))
    name = CharField(
        label=u"Имя", 
        max_length=30, 
        widget=TextInput({ "placeholder": "Петр" }))
    patronymic = CharField(
        label=u"Отчество", 
        max_length=30, 
        widget=TextInput({ "placeholder": "Иванович" }))
    born_date = DateField(
        label=u'Дата рождения', 
        widget=TextInput({"placeholder":"ДД/ММ/ГГГГ"}), 
        input_formats=['%d/%m/%Y','%d-%m-%Y'], initial='01/01/1997')
    sex = ChoiceField(
        label=u'Пол', 
        choices=((u'М',u'Мужской'),(u'Ж',u'Женский')), 
        widget=RadioSelect())    


class Step_Document(Form):
    id_doc = ModelChoiceField(
        label=u'Вид документа',
        queryset=Universal_directory.objects.filter(
            type=Directory_types.objects.get(name=u'Документ')))
    doc_serial = CharField(
        label=u"Серия и №", 
        max_length=10, 
        widget=TextInput({"placeholder":"9811555555"}))
    doc_distributed_date = DateField(
        label=u'Дата выдачи',
        widget=TextInput({"placeholder":"ДД/ММ/ГГГГ"}), 
        input_formats=['%d/%m/%Y','%d-%m-%Y'])
    doc_distributed_organisation = CharField(
        label=u"Кем выдан", 
        max_length=100, 
        widget=TextInput({"placeholder":"Nским УВД"}))


class Step_Education(Form):
    prev_edu_level = ModelChoiceField(
        label=u'Образование',
        queryset=Universal_directory.objects.filter(
            type=Directory_types.objects.get(name=u'Образование')))
    prev_edu_organisation = ModelChoiceField(
        label=u'Учебное заведение', 
        queryset=Universal_directory.objects.filter(
            type=Directory_types.objects.get(name=u'Учебное заведение')),
        required=False)
    prev_edu_organisation_name = CharField(
        label=u'Учебное заведение', 
        required=False)
    prev_edu_doc_type = ModelChoiceField(
        label=u'Вид документа об образовании', 
        queryset=Universal_directory.objects.filter(
            type=Directory_types.objects.get(name=u'Документ об образовании')))
    prev_edu_doc_seria = CharField(
        label=u"Серия",
        max_length=10)
    prev_edu_doc_num = CharField(
        label=u"Номер",
        max_length=30)


class Step_Address(Form):
    id_adm_territory = ModelChoiceField(
        label=u'Республика/край/область',
        queryset=Universal_directory.objects.filter(
            type=Directory_types.objects.get(name=u'Субъект федерации')),
        initial=15)
    id_adm_unit = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Муниципальный район')), label=u'Район\улус', required=False)
    adm_unit_name = CharField(label='Район\улус', required=False)
    id_settlement = ModelChoiceField(queryset=Universal_directory.objects.filter(type=Directory_types.objects.get(name=u'Населённый пункт')), label=u'Город\село', required=False)
    settlement_name = CharField(label='Город\село', required=False)
    post_index = CharField(label='Индекс', required=False)
    block_no = CharField(label='Корпус', required=False)
    apart_no = CharField(label='Квартира', required=False)
    def __init__(self, *args, **kwargs):
        super(Step_Address, self).__init__(*args, **kwargs)
        if 0 == len(self.data):
            self.fields['id_adm_unit'].queryset = Universal_directory.objects.none()
            self.fields['id_settlement'].queryset = Universal_directory.objects.filter(parent=None,type=Directory_types.objects.get(name=u'Населённый пункт'))
    def clean(self):
        cleaned_data = super(Step_Address, self).clean()
        id_adm_unit = cleaned_data.get('id_adm_unit')
        adm_unit_name = cleaned_data.get('adm_unit_name')
        id_settlement = cleaned_data.get('id_settlement')
        settlement_name = cleaned_data.get('settlement_name')
        if not id_settlement and not settlement_name:
            msg = u'Обязательное поле'
            self._errors['id_settlement'] = self.error_class([msg])
            self._errors['settlement_name'] = self.error_class([msg])
            del cleaned_data['id_settlement']
            del cleaned_data['settlement_name']
        if not id_adm_unit and adm_unit_name:
            if 0 == Universal_directory.objects.filter(name=cleaned_data['adm_unit_name'],type=Directory_types.objects.get(name=u'Муниципальный район (пользовательский ввод)')).count():
                Universal_directory(name=cleaned_data['adm_unit_name'],type=Directory_types.objects.get(name=u'Муниципальный район (пользовательский ввод)')).save()
            cleaned_data['id_adm_unit'] = Universal_directory.objects.get(name=cleaned_data['adm_unit_name'],type=Directory_types.objects.get(name=u'Муниципальный район (пользовательский ввод)'))
        if not id_settlement and settlement_name:
            if 0 == Universal_directory.objects.filter(name=cleaned_data['settlement_name'],type=Directory_types.objects.get(name=u'Населённый пункт (пользовательский ввод)')).count():
                Universal_directory(name=cleaned_data['settlement_name'],type=Directory_types.objects.get(name=u'Населённый пункт (пользовательский ввод)')).save()
            cleaned_data['id_settlement'] = Universal_directory.objects.get(name=cleaned_data['settlement_name'],type=Directory_types.objects.get(name=u'Населённый пункт (пользовательский ввод)'))
        return cleaned_data
    class Meta:
        model = Address
        fields = ('id_adm_territory', 'id_adm_unit', 'adm_unit_name', 'id_settlement', 'settlement_name', 'post_index', 'street_name', 'house_no', 'block_no', 'apart_no')
