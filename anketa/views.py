# -*- coding: utf-8 -*-
import json
import numpy as np
import datetime

from django.views.generic.edit import CreateView
from django.forms.formsets import formset_factory
from django.utils import timezone
from django.db.models import Sum

from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template import RequestContext
from kladr.models import Street, Kladr
from anketa.models import Person, Address, Attribute, AttrValue, Abiturient, EduOrg, ProfileAttrs, ApplicationProfiles, \
	Education_Prog, Profile, Application, EduForm, ApplicationProfiles, Milit, Docs, Exams, DocAttr, Education, \
	Contacts, Relation, Exams_needed, Achievements, Privilegies, DocImages, Application_attrs
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required


def StartPage(request):
	return render(request, 'anketa/start.html')


def StartApp(request):
	return render(request, 'anketa/wizardform.html')


@login_required(login_url='authapp:index')
def PersonProfile(request):
	person = Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	args = {'currentpage': 1}
	args1 = []
	applications = Application.objects.filter(abiturient__user=request.user).filter(track=True).filter(
		date__year=datetime.datetime.strftime(datetime.datetime.today(), "%Y"))
	if applications is not None:
		appProf = ApplicationProfiles.objects.all()
		for app in applications:
			prof = appProf.filter(application__id=app.id).first()
			args1.append({'app': app, 'prof': prof})
		args['applications'] = args1
	args.update(csrf(request))
	return render(request, 'anketa/profile.html', args)


@login_required(login_url='authapp:index')
def PersonData(request):
	args = {'currentpage': 2}
	person = Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	# 1
	args['fname'] = person.fname
	args['sname'] = person.sname
	args['mname'] = person.mname
	args['birthdate'] = person.birthdate
	args['sex'] = person.sex
	if person.birthplace is not None:
		args['birthplace'] = person.birthplace
	if person.citizenship is not None:
		args['citizenship'] = person.citizenship.value
		args['citizenship_id'] = person.citizenship.id
	if person.nationality is not None:
		args['nationality'] = person.nationality.value
		args['nationality_id'] = person.nationality.id
	# 2
	doctype = person.docs_set.filter(docType__attribute__name__icontains=u'удостоверяющего личность').first()
	if doctype is not None:
		args['doctype'] = doctype.docType.value
		args['doctype_id'] = doctype.docType.id
		args['doctype_serial'] = doctype.serialno
		args['doctype_number'] = doctype.number
		args['doctype_date'] = doctype.issueDate
		args['doctype_issuer_id'] = doctype.docIssuer.id
		args['doctype_issuer'] = doctype.docIssuer.value
	if person.education_set.first():
		edudoctype = person.education_set.first()
		args['edudoctype'] = edudoctype.doc.docType.value
		args['edudoctype_id'] = edudoctype.doc.docType.id
		args['edudoctype_serial'] = edudoctype.doc.serialno
		args['edudoctype_number'] = edudoctype.doc.number
		args['datejoining'] = edudoctype.enterDate
		args['dateexiting'] = edudoctype.graduationDate
		args['prevedu'] = edudoctype.level.value
		args['preveduname'] = edudoctype.eduOrg.name
		args['preveduname_id'] = edudoctype.eduOrg.id
	if person.docs_set.filter(docType__value__icontains='СНИЛС').first() is not None:
		args['inila'] = person.docs_set.filter(docType__value__icontains='СНИЛС').first().number

	if DocImages.objects.filter(doc=person.docs_set.filter(
			docType__attribute__name__icontains='удостоверяющего личность').first()):
		docs_images = []
		for docs_image in DocImages.objects.filter(doc=person.docs_set.filter(
			docType__attribute__name__icontains='удостоверяющего личность').first()):
			docs_images.append(docs_image.image)
		args['docs_images'] = docs_images

	if DocImages.objects.filter(doc=person.docs_set.filter(
			docType__attribute__name__icontains='Вид документа об образовании').first()):
		edudocs_images = []
		for edudocs_image in DocImages.objects.filter(doc=person.docs_set.filter(
			docType__attribute__name__icontains='Вид документа об образовании').first()):
			edudocs_images.append(edudocs_image.image)
		args['edudocs_images'] = edudocs_images

	if DocImages.objects.filter(doc=person.docs_set.filter(
			docType__value='СНИЛС').first()):
		inila_images = []
		for inila_image in DocImages.objects.filter(doc=person.docs_set.filter(
			docType__value='СНИЛС').first()):
			inila_images.append(inila_image.image)
		args['inila_images'] = inila_images

	args_to_print = [
		'doctype',
		'doctype_id',
		'doctype_serial',
		'doctype_number',
		'doctype_date',
		'doctype_issuer_id',
		'doctype_issuer',
		'edudoctype',
		'edudoctype_id',
		'edudoctype_serial',
		'edudoctype_number',
		'datejoining',
		'dateexiting',
		'prevedu',
		'preveduname',
		'preveduname_id',
		'inila',
		'docs_images',
		'edudocs_images',
		'inila_images',
	]
	for arg_to_print in args_to_print:
		try:
			print(arg_to_print + ': ' + str(args[arg_to_print]))
		except:
			print(arg_to_print + ': ')

	# 3
	def get_full_address(street_code, house, building, flat):
		region_object = Kladr.objects.filter(code=(street_code[:2] + '00000000000')).first()
		region = region_object.name + ' ' + region_object.socr + '.'
		district_object = Kladr.objects.filter(code=(street_code[:5] + '00000000')).first()
		if street_code[2:5] != '000':
			district = district_object.name + ' ' + district_object.socr + '.'
		else:
			district = ''
		city_object = Kladr.objects.filter(code=(street_code[:8] + '00000')).first()
		if street_code[5:8] != '000':
			city = city_object.socr + '. ' + city_object.name
		else:
			city = ''
		village_object = Kladr.objects.filter(code=(street_code[:11] + '00')).first()
		if street_code[8:11] != '000':
			village = village_object.socr + '. ' + village_object.name
		else:
			village = ''
		street_object = Street.objects.filter(code=street_code).first()
		street = street_object.socr + '. ' + street_object.name
		result = region
		if district:
			result += ', ' + district
		if city:
			result += ', ' + city
		if village:
			result += ', ' + village
		result += ', ' + street
		result += ', ' + house
		if building:
			result += ' корпус ' + building
		if flat:
			result += ', кв. ' + flat
		return result

	address = person.address_set.filter(adrs_type__value__icontains='По прописке').first()
	if address is not None:
		args['adrsp'] = get_full_address(address.street.code, address.house, address.building, address.flat)
		args['streetp'] = address.street.code
		args['housep'] = address.house
		args['buildingp'] = address.building
		args['flatp'] = address.flat
		if address.adrs_type_same:
			args['adrsisthesame'] = 'yes'
		else:
			args['adrsisthesame'] = 'no'
	address = person.address_set.filter(adrs_type__value__icontains='Фактический').first()
	if address is not None:
		args['adrsf'] = get_full_address(address.street.code, address.house, address.building, address.flat)
		args['streetf'] = address.street.code
		args['housef'] = address.house
		args['buildingf'] = address.building
		args['flatf'] = address.flat

	"""args_to_print = [
		'adrsp',
		'streetp',
		'housep',
		'buildingp',
		'flatp',
		'adrsf',
		'streetf',
		'housef',
		'buildingf',
		'flatf',
		'adrsisthesame',
	]
	for arg_to_print in args_to_print:
		try:
			print(arg_to_print + ': ' + args[arg_to_print])
		except:
			print(arg_to_print + ': ' )"""

	contacts_type = AttrValue.objects.filter(attribute__name__icontains=u'Тип контакта')
	if contacts_type is not None:
		args['contacts_type'] = contacts_type
	person_contacts = person.contacts_set.all()
	if person_contacts is not None:
		contacts = []
		for item in person_contacts:
			cont = {}
			cont['type'] = item.contact_type
			cont['value'] = item.value
			contacts.append(cont)
		args['contacts'] = contacts

	relation_type = AttrValue.objects.filter(attribute__name__icontains=u'Тип связи')
	if relation_type is not None:
		args['relation_type'] = relation_type
	if Relation.objects.filter(abiturient=person) is not None:
		person_relations = Relation.objects.filter(abiturient=person)
		relations = []
		for item in person_relations:
			cont = {}
			cont['type'] = item.relType
			cont['fio'] = item.person.fullname
			cont['value'] = Contacts.objects.filter(person=item.person).first().value
			relations.append(cont)
		args['relation'] = relations

	# 4
	exams = person.exams_set.exclude(exam_examType__value=u'Вступительный').all()
	if exams is not None:
		examsList = []
		for item in exams:
			exam = {}
			exam['id'] = item.id
			exam['subject'] = item.exam_subjects.id
			exam['subject_value'] = item.exam_subjects.value
			exam['points'] = item.points
			exam['year'] = item.year
			exam['examtype'] = {'id': item.exam_examType.id, 'name': item.exam_examType.value}
			examsList.append(exam)
		args['exams'] = examsList
	add_exams = person.exams_set.filter(exam_examType__value=u'Вступительный')
	if add_exams is not None:
		specusl = False
		addExamsList = []
		for item in add_exams:
			exam = {}
			exam['id'] = item.id
			exam['subject'] = item.exam_subjects.id
			exam['subject_value'] = item.exam_subjects.value
			exam['points'] = item.points
			exam['year'] = item.year
			if item.special and specusl == False:
				args['specusl'] = True
			addExamsList.append(exam)
		args['addExams'] = addExamsList
	# 5
	privilegies = person.privilegies_set.all()
	if privilegies is not None:
		privList = []
		for item in privilegies:
			priv = {}
			priv['id'] = item.id
			priv['privcat'] = {'id': item.category.id, 'name': item.category.value}
			priv['privtype'] = {'id': item.priv_type.id, 'name': item.priv_type.value}
			privList.append(priv)
		args['privilegies'] = privList
	achievements = person.achievements_set.all()
	if achievements is not None:
		achievList = []
		for item in achievements:
			achiev = {}
			achiev['id'] = item.id
			achiev['achievement'] = {'id': item.contest.id, 'name': item.contest.value}
			achiev['achievresult'] = {'id': item.result.id, 'name': item.result.value}
			achiev['achievDoc'] = 0
			achievList.append(achiev)
		args['achievements'] = achievList

	# 7
	args['hostel'] = person.hostel
	milit = Milit.objects.filter(abiturient=person).first()
	if milit is not None:
		args['liableForMilit'] = milit.liableForMilit
		if milit.liableForMilit == True:
			args['isServed'] = milit.isServed
			if milit.isServed == True:
				if milit.rank is not None:
					args['rank'] = milit.rank.value
					args['rank_id'] = milit.rank.id
				args['yeararmy'] = milit.yearDismissial
	if person.foreign_lang is not None:
		args['flang_id'] = person.foreign_lang.id
		args['flang'] = person.foreign_lang.value
	# print(args)
	args.update(csrf(request))
	return render(request, 'anketa/persondata.html', args)


@login_required(login_url='authapp:index')
def Applications(request):
	args = {'currentpage': 3}
	args1 = []
	year = datetime.datetime.strftime(datetime.datetime.today(), "%Y")
	person = Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	applications = Application.objects.filter(abiturient__user=request.user).filter(date__year=year).exclude(
		appState=AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(
			value__icontains=u'Анулированный').first())
	appProf = ApplicationProfiles.objects.all()
	for app in applications:
		prof = appProf.filter(application__id=app.id)
		args1.append({'app': app, 'prof': prof})

	args['applications'] = args1
	return render(request, 'anketa/applicationList.html', args)


@login_required(login_url='authapp:index')
def Account(request):
	args = {'currentpage': 4}
	person = Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	args['email'] = request.user.email
	args.update(csrf(request))
	return render(request, 'anketa/account.html', args)


def GetSelectedApplication(request):
	result = {}
	application = Application.objects.select_related().get(pk=request.GET.get('id', ''))
	target = Application_attrs.objects.filter(app__id=application.id).first()
	if target is not None:
		result['target'] = True
	else:
		result['target'] = False
	result['app_num'] = application.id
	result['eduprior'] = application.priority
	app_profiles = ApplicationProfiles.objects.select_related().filter(application=application)
	result['department_id'] = application.department.id
	result['department_name'] = application.department.name
	result['track'] = application.track
	result['budget'] = application.budget
	result['withfee'] = application.withfee
	result['edu_prog_id'] = app_profiles.first().profile.profile.edu_prog.id
	result[
		'edu_prog_name'] = app_profiles.first().profile.profile.edu_prog.name + ' ' + app_profiles.first().profile.profile.edu_prog.qualification.value
	result['edu_prog_eduform_id'] = app_profiles.first().profile.id
	# result['edu_prog_eduform_name']=[x[1] for x in EduForm if x[0] == app_profiles.first().profile.eduform][0]
	profiles = []
	for item in app_profiles:
		profiles.append(
			{'id': item.profile.profile.id, 'profile': item.profile.profile.name, 'eduform': item.profile.eduform,
			 'prof_attr_id': item.profile.id, 'app_prof_id': item.id})
	result['profiles'] = profiles
	result['profiles_len'] = len(profiles)
	return HttpResponse(json.dumps(result), content_type="application/json")


# def save_exams


@transaction.atomic
def SaveExam(request, abit):
	print('Saving Exam!!')
	# if abit.exams_set.filter(exam_examType__value=u'ЕГЭ') is not None:
	#	Exams.objects.filter(abiturient__id=abit.id).filter(exam_examType__value=u'ЕГЭ').delete()
	# abit.exams_set.all().delete a cho ne rabotaet
	# examtype = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').filter(value__icontains=u'ЕГЭ').first()

	exam_details = {'ege': list(
		zip(request.POST.getlist('egeDisc'), request.POST.getlist('examType'), request.POST.getlist('egeYear'),
			request.POST.getlist('egePoints'), [False] * len(request.POST.getlist('egeDisc'))))}
	if len(request.POST.getlist('addDisc')) > 0:
		specusl = False
		if request.POST.get('specusl', '') == "yes":
			specusl = True
		examtype_id = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').filter(
			value=u'Вступительный').first().id
		exam_details['add'] = list(
			zip(request.POST.getlist('addDisc'), [examtype_id] * len(request.POST.getlist('addDisc')),
				[datetime.date.today().year] * len(request.POST.getlist('addDisc')),
				[0] * len(request.POST.getlist('addDisc')), [0] * len(request.POST.getlist('addDisc')),
				[specusl] * len(request.POST.getlist('addDisc'))))
	print(exam_details)
	for key in exam_details.keys():
		for i in range(len(exam_details[key])):
			subject = AttrValue.objects.filter(attribute__name__icontains=u'Дисциплина').filter(
				pk=exam_details[key][i][0]).first()
			examtype = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').filter(
				pk=exam_details[key][i][1]).first()
			# проверить присутствует ли экзамен по типу, дисциплине и году
			exam = Exams.objects.filter(abiturient__id=abit.id, exam_examType__id=exam_details[key][i][1],
										exam_subjects=exam_details[key][i][0], year=exam_details[key][i][2]).first()
			if exam is None:
				exam = Exams()
				exam.abiturient = abit
				exam.exam_examType = examtype
				exam.exam_subjects = subject
				exam.year = exam_details[key][i][2]
			exam.special = exam_details[key][i][4]
			if key != 'add':
				exam.points = exam_details[key][i][3]
			exam.save()
	# if len(request.POST.get('additionalExams', '')) > 0:
	# 	#add_exams = request.POST.get('additionalExams', '').split(',')
	# 	specusl = False
	# 	if request.POST.get('specusl', '') == "yes":
	# 		specusl = True
	# 	if abit.exams_set.filter(exam_examType__value=u'Вступительный') is not None:
	# 		Exams.objects.filter(abiturient=abit).filter(exam_examType__value=u'Вступительный').delete()
	# 	for item in exam_details['add']:
	# 		add_exam = Exams()
	# 		add_exam.abiturient = abit
	# 		add_exam.exam_examType = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').filter(
	# 			value__icontains=u'Вступительный').first()
	# 		add_exam.exam_subjects = AttrValue.objects.filter(attribute__name__icontains=u'Дисциплина').filter(
	# 			pk=item).first()
	# 		add_exam.year = datetime.date.today().year
	# 		add_exam.special = specusl
	# 		add_exam.save()
	print('Added!')
	print(exam_details)


@transaction.atomic
def SavePrivilegies(request, abit):
	priv_details = list(zip(request.POST.getlist('privcat'), request.POST.getlist('privtype')))
	achiev_details = list(zip(request.POST.getlist('achievement'), request.POST.getlist('achievresult'),
							  request.POST.getlist('achievDoc')))
	print(priv_details)
	print(achiev_details)
	for i in range(len(priv_details)):
		privcat = AttrValue.objects.filter(attribute__name__icontains=u'Категория').filter(
			pk=priv_details[i][0]).first()
		privtype = AttrValue.objects.filter(attribute__name__icontains=u'Тип привелегии').filter(
			pk=priv_details[i][1]).first()
		priv = Privilegies.objects.filter(abiturient__id=abit.id, category__id=priv_details[i][0],
										  priv_type__id=priv_details[i][1], ).first()
		if priv is None:
			priv = Privilegies()
			priv.abiturient = abit
			priv.category = privcat
			priv.priv_type = privtype

		priv.save()
		print('Priv save!')

	for i in range(len(achiev_details)):
		achievement = AttrValue.objects.filter(attribute__name__icontains=u'Мероприятие').filter(
			pk=achiev_details[i][0]).first()
		achievresult = AttrValue.objects.filter(attribute__name__icontains=u'Достигнутый результат').filter(
			pk=achiev_details[i][1]).first()
		achiev = Achievements.objects.filter(abiturient__id=abit.id, contest__id=achiev_details[i][0],
											 result__id=achiev_details[i][1]).first()
		if achiev is None:
			achiev = Achievements()
			achiev.abiturient = abit
			achiev.contest = achievement
			achiev.result = achievresult
		achiev.save()
		print('Achiev save!')


@transaction.atomic
def SaveAddress(request, abit):
	print('Saving Address')
	Address.objects.filter(abiturient=abit).delete()
	address_type = 'По прописке'
	address = Address()
	address.abiturient = abit
	address.adrs_type = AttrValue.objects.filter(value__icontains=address_type).first()
	address.street = Street.objects.filter(code=request.POST.get('streetp', '')).first()
	address.house = request.POST.get('housep', '')
	address.building = request.POST.get('buildingp', '')
	address.flat = request.POST.get('flatp', '')
	if request.POST.get('adrsisthesame', '') == "yes":
		address.adrs_type_same = True
	else:
		address.adrs_type_same = False
	address.save()
	if request.POST.get('adrsisthesame', '') == "no":
		address_type = 'Фактический'
		address = Address()
		address.abiturient = abit
		address.adrs_type = AttrValue.objects.filter(value__icontains=address_type).first()
		address.street = Street.objects.filter(code=request.POST.get('streetf', '')).first()
		address.house = request.POST.get('housef', '')
		address.building = request.POST.get('buildingf', '')
		address.flat = request.POST.get('flatf', '')
		address.adrs_type_same = False
		address.save()
	print('Address saved')


@transaction.atomic
def SaveContacts(request, abit):
	print('Saving Contacts')
	contacttype = request.POST.getlist('contacttype')
	contactvalue = request.POST.getlist('contactvalue')
	if len(contactvalue) < 1 or len(contacttype) < 1:
		return
	if abit.contacts_set.all() is not None:
		Contacts.objects.filter(person=abit).delete()

	for i in range(len(contacttype)):
		if len(contacttype[i]) > 0 and len(contactvalue[i]) > 0:
			# contact = Contacts.objects.filter(person__id = abit.id, contact_type = contacttype[i], value = contactvalue[i]).first()
			# if contact is None:
			contact = Contacts()
			contact.person = abit
			contact.contact_type = AttrValue.objects.filter(pk=contacttype[i]).first()
			contact.value = contactvalue[i]
			contact.save()


@transaction.atomic
def SaveRelevants(request, abit):
	print('Saving Relevants')
	relationtype = request.POST.getlist('relationtype')
	relationcontactvalue = request.POST.getlist('relationcontactvalue')
	relationFIO = request.POST.getlist('relationFIO')
	if Relation.objects.filter(abiturient=abit) is not None:
		Relation.objects.filter(abiturient=abit).delete()
	for i in range(0, len(relationtype)):
		if len(relationtype[i]) > 0 and len(relationcontactvalue[i]) > 0 and len(relationFIO[i]) > 0:
			relation = Relation()
			relation.abiturient = abit
			relation.relType = AttrValue.objects.filter(pk=relationtype[i]).first()
			relperson = Person()
			fio = relationFIO[i].split(' ')
			if fio[0]:
				relperson.sname = fio[0]
			if fio[1]:
				relperson.fname = fio[1]
			if fio[2]:
				relperson.mname = fio[2]
			relperson.sex = "М"
			relperson.birthdate = datetime.datetime.strptime('15/05/2007', '%d/%m/%Y').strftime('%Y-%m-%d')
			relperson.save()
			relation.person = relperson
			contact = Contacts()
			contact.person = relperson
			contact.contact_type = AttrValue.objects.filter(value__icontains=u'телефон').first()
			contact.value = relationcontactvalue[i]
			contact.save()
			relation.save()


def SaveContactDetails(request, abit):
	print('Saving Contact Details')
	SaveAddress(request, abit)
	SaveContacts(request, abit)
	SaveRelevants(request, abit)


@transaction.atomic
def SaveOther(request, abit):
	if (len(request.POST.get('hostel', ''))) > 0:
		abit.hostel = False
		if (request.POST.get('hostel', '') == "yes"):
			abit.hostel = True
	if (len(request.POST.get('flang', ''))) > 0:
		abit.foreign_lang = AttrValue.objects.get(pk=request.POST.get('flang', ''))

	if Milit.objects.filter(abiturient=abit).first() is not None:
		Milit.objects.filter(abiturient=abit).first().delete()
	milit = Milit()
	milit.abiturient = abit
	if (len(request.POST.get('liableForMilit', ''))) > 0:
		if request.POST.get('liableForMilit', '') == "yes":
			milit.liableForMilit = True
			if (len(request.POST.get('isServed', ''))) > 0:
				if request.POST.get('isServed', '') == "yes":
					milit.isServed = True
					if (len(request.POST.get('rank', ''))) > 0:
						milit.rank = AttrValue.objects.get(pk=request.POST.get('rank'))
					if (len(request.POST.get('yeararmy', ''))) > 0:
						milit.yearDismissial = int(request.POST.get('yeararmy', ''))
			# АХАХАХАХАХ ХКАКОЙ ККРАСИВЫЙ КОД АХАХАХАХАХХААХХА
	milit.save()


def AddDataToPerson(request):
	print('Add Data to Person')
	result = {'result': "success"}
	# print(request.POST)
	if request.method == 'POST':
		try:
			page = int(request.POST.get('currentPage', ''))
			abit = Abiturient.objects.get(user=request.user)
			if abit.info_progress is None:
				abit.info_progress = "000000"
			# progress = abit.info_progress.split()
			if page == 1:  # Личные данные
				# pageIsComplete=True;
				print('Personal')
				abit.sname = request.POST.get('sname', '')
				abit.fname = request.POST.get('name', '')
				abit.mname = request.POST.get('mname', '')
				abit.birthplace = request.POST.get('birthplace', '')
				if (len(request.POST.get('birthday', ''))) > 0:
					abit.birthdate = datetime.datetime.strptime(request.POST.get('birthday', ''), '%d/%m/%Y').strftime(
						'%Y-%m-%d')
				if (len(request.POST.get('nation', ''))) > 0:
					abit.nationality = AttrValue.objects.get(pk=request.POST.get('nation', ''))
				if (len(request.POST.get('citizenship', ''))) > 0:
					abit.citizenship = AttrValue.objects.get(pk=request.POST.get('citizenship', ''))
				if (len(request.POST.get('sex', ''))) > 0:
					abit.sex = request.POST.get('sex', '')
			if page == 2:
				for i in range(int(request.POST.get('removedDocsImages', ''))):
					DocImages.objects.filter(image=request.POST.get('removedDocsImage' + str(i))).delete()
					print('removed: ' + request.POST.get('removedDocsImage' + str(i)))

				for i in range(int(request.POST.get('removedEduDocsImages', ''))):
					DocImages.objects.filter(image=request.POST.get('removedEduDocsImage' + str(i))).delete()
					print('removed: ' + request.POST.get('removedEduDocsImage' + str(i)))

				for i in range(int(request.POST.get('removedInilaImages', ''))):
					DocImages.objects.filter(image=request.POST.get('removedInilaImage' + str(i))).delete()
					print('removed: ' + request.POST.get('removedInilaImage' + str(i)))

				doctype = abit.docs_set.filter(docType__attribute__name__icontains='удостоверяющего личность').first()
				if doctype is None:
					doctype = Docs()
					doctype.abiturient = abit
				else:
					doctype.number = None
					doctype.serialno = None
					doctype.issueDate = None
				if (len(request.POST.get('doctype', '')) > 0):
					doctype.docType = AttrValue.objects.get(pk=request.POST.get('doctype', ''))
				if (len(request.POST.get('serialdoc', '')) > 0):
					doctype.serialno = int(request.POST.get('serialdoc', ''))
				if (len(request.POST.get('numberdoc', '')) > 0):
					doctype.number = int(request.POST.get('numberdoc', ''))
				if (len(request.POST.get('datedoc', '')) > 0):
					doctype.issueDate = datetime.datetime.strptime(request.POST.get('datedoc', ''),
																   '%d/%m/%Y').strftime('%Y-%m-%d')
				if (len(request.POST.get('docissuer', '')) > 0):
					doctype.docIssuer = AttrValue.objects.get(pk=request.POST.get('docissuer', ''))
				print(doctype)
				doctype.save()

				print('Saving doc image')
				for file in request.FILES.getlist('docs_images'):
					print(file.name)
					doc_image = DocImages()
					doc_image.doc = abit.docs_set.filter(
						docType__attribute__name__icontains='удостоверяющего личность').first()
					doc_image.image = file
					doc_image.save()

				print('Saving Edu')
				docs = Docs.objects.filter(abiturient=abit,
									docType__attribute__name__icontains='Вид документа об образовании').first()
				if docs is None:
					docs = Docs()
				docs.abiturient = abit
				docs.docType = AttrValue.objects.get(pk=request.POST.get('edudoctype', ''))
				docs.serialno = int(request.POST.get('serialedudoc', ''))
				docs.number = int(request.POST.get('numberedudoc', ''))
				docs.docIssuer = None
				print(docs.abiturient)
				print(docs.docType)
				print(docs.serialno)
				print(docs.number)
				print(docs.docIssuer)
				print(docs)
				docs.save()

				education = Education.objects.filter(abiturient=abit).first()
				if education is None:
					education = Education()
				education.abiturient = abit
				education.doc = Docs.objects.filter(
					abiturient=abit,
					docType__attribute__name__icontains='Вид документа об образовании'
				).first()
				if request.POST.get('prevedu', '') == 'soo':
					education.level = AttrValue.objects.filter(value='СОО').first()
				if request.POST.get('prevedu', '') == 'npo':
					education.level = AttrValue.objects.filter(value='НПО').first()
				if request.POST.get('prevedu', '') == 'spo':
					education.level = AttrValue.objects.filter(value='СПО').first()
				if request.POST.get('prevedu', '') == 'vpo':
					education.level = AttrValue.objects.filter(value='ВПО').first()
				education.enterDate = datetime.datetime.strptime(request.POST.get('datejoining', ''),
																 '%d/%m/%Y').strftime('%Y-%m-%d')
				education.graduationDate = datetime.datetime.strptime(request.POST.get('dateexiting', ''),
																	  '%d/%m/%Y').strftime('%Y-%m-%d')
				education.eduOrg = EduOrg.objects.get(pk=request.POST.get('preveduname', ''))
				print(education.abiturient)
				print(education.doc)
				print(education.level)
				print(education.enterDate)
				print(education.graduationDate)
				print(education.eduOrg)
				education.save()

				print('Saving edu doc image')
				for file in request.FILES.getlist('edudocs_images'):
					print(file.name)
					doc_image = DocImages()
					doc_image.doc = abit.docs_set.filter(
						docType__attribute__name__icontains='Вид документа об образовании').first()
					doc_image.image = file
					doc_image.save()

				print('Saving INILA')
				inila = Docs.objects.filter(abiturient=abit, docType__value='СНИЛС').first()
				if inila is None:
					inila = Docs()
				inila.abiturient = abit
				inila.number = int(request.POST.get('inila', ''))
				inila.docType = AttrValue.objects.filter(value='СНИЛС').first()
				print(inila.abiturient)
				print(inila.number)
				print(inila.docType)
				inila.save()

				print('Saving inila image')
				for file in request.FILES.getlist('inila_images'):
					print(file.name)
					doc_image = DocImages()
					print(abit.docs_set.filter(docType__value='СНИЛС').first())
					doc_image.doc = abit.docs_set.filter(docType__value='СНИЛС').first()
					doc_image.image = file
					doc_image.save()

			if page == 3:
				print('Saving Page 3 - Contacts')
				SaveContactDetails(request, abit)

			if page == 4:
				print('Exams')
				SaveExam(request, abit)

			if page == 5:
				SavePrivilegies(request, abit)

			if page == 6:
				SaveOther(request, abit)

			abit.save()

		except Exception as e:
			result['result'] = str(e)
	print('result!')
	return HttpResponse(json.dumps(result), content_type="application/json")


@transaction.atomic
def SaveApplication(request):
	result = {'result': 0, 'error_msg': ''}
	if request.method == 'POST':
		if (int(request.POST.get('facepalm', '')) > 0):
			application = Application.objects.get(pk=request.POST.get('facepalm'))
			if application.appState == AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(
					value__icontains=u'Подтвержденный').first():
				result = {'result': 0, 'error_msg': 'zayavlenie yje podtverjdeno nelzya menyat lul'}
				return HttpResponse(json.dumps(result), content_type="application/json")
		else:
			application = Application()
		application.abiturient = Abiturient.objects.get(user=request.user)
		application.department = EduOrg.objects.get(pk=request.POST.get('department', ''))
		dateNow = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
		application.date = dateNow
		app_status = AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(
			value__icontains=u'Подан').first()
		application.appState = app_status
		application.points = 100  # checkpoint
		application.priority = request.POST.get('eduprior')
		if request.POST.get('track', '') == "false":
			application.track = False
		else:
			application.track = True
		min1 = 0
		if request.POST.get('budget', ''):
			application.budget = True
			min1 += 1
		else:
			application.budget = False
		if request.POST.get('withfee', ''):
			application.withfee = True
			min1 += 1
		else:
			application.withfee = False

		#######################ЦЕЛЕВОЕ####################################

		if request.POST.get('target',''):
			fiks1 = 1
			min1 += 1
		else:
			targetApp = Application_attrs.objects.filter(app__id=application.id).first()
			if targetApp is not None:
				targetApp.delete()
		#######################ЦЕЛЕВОЕ####################################

		if min1 == 0:
			result = {'result': 0, 'error_msg': 'minimym 1 chek viberi'}
			return HttpResponse(json.dumps(result), content_type="application/json")

		#######################ЛЬГОТЫ####################################
		if len(Privilegies.objects.filter(abiturient__id=Abiturient.objects.get(user=request.user).id))>0:
			fiks2 = 1
		else:
			privilegesApp = Application_attrs.objects.filter(app__id=application.id).first()
			if privilegesApp is not None:
				privilegesApp.delete()
		#######################ЛЬГОТЫ####################################

		if (len(request.POST.getlist('eduprof'))>0):
			forms = request.POST.getlist('eduform','')
			app_prof_id = request.POST.getlist('prof_id','')
			##############delete################
			ppc=[x for x in app_prof_id if x != -1]
			if len(ppc)<len(ApplicationProfiles.objects.filter(application=application)):
				ApplicationProfiles.objects.filter(application=application).exclude(id__in=ppc).delete()
			##############delete################
			abit_exams = Exams.objects.filter(abiturient=application.abiturient)#EXAMS###########################
			points_summ=0
			for i in abit_exams:
				if i.points is not None:
					points_summ+=i.points#checkpoint
			forms = list(set(forms))
			for i in range(len(forms)):
				profile = ProfileAttrs.objects.get(pk=forms[i])
				if dateNow >= datetime.datetime.strftime(profile.startDate,'%Y-%m-%d'):
					if dateNow <= datetime.datetime.strftime(profile.endDate,'%Y-%m-%d'):
						application.save()

						if fiks1 ==	1:
							targetApp = Application_attrs()
							targetApp.app = application
							targetApp.attribute = AttrValue.objects.filter(attribute__name__icontains=u'Тип договора образования').filter(value__icontains=u'Целевой').first()
							if Application_attrs.objects.filter(app__id=application.id,attribute__id=AttrValue.objects.filter(attribute__name__icontains=u'Тип договора образования').filter(value__icontains=u'Целевой').first().id)is not None:
								targetApp.save()

						if fiks2 == 1:
							privilegesApp = Application_attrs()
							privilegesApp.app = application
							privilegesApp.attribute = AttrValue.objects.filter(attribute__name__icontains=u'Тип договора образования').filter(value__icontains=u'Льготный').first()
							if Application_attrs.objects.filter(app__id=application.id,attribute__id=AttrValue.objects.filter(attribute__name__icontains=u'Тип договора образования').filter(value__icontains=u'Льготный').first().id)is not None:
								privilegesApp.save()

						appProf = ApplicationProfiles.objects.filter(pk = app_prof_id[i]).first()
						if appProf is None:
							appProf = ApplicationProfiles()
						appProf.application=application
						appProf.profile=ProfileAttrs.objects.get(pk = forms[i])
						appProf.points=points_summ
						exams_needed = Exams_needed.objects.filter(profile=appProf.profile.profile)
						for exam_need in exams_needed:
							for abit_exam in abit_exams:
								if abit_exam.exam_subjects==exam_need.subject:
									if abit_exam.points<exam_need.min_points:
										result = {'result':0, 'error_msg':'yBbl He xBoTaeT 6aJIJIoB'}
										return HttpResponse(json.dumps(result), content_type="application/json")
										#########FIX IT###############
								#else:
									#result = {'result':0, 'error_msg':'yBbl He xBoTaeT Heo6xoDuMblx ek3aMeHoB'}
						appProf.save()
					else:
						result = {'result':0, 'error_msg':'АЛЛО гараж период приема заявлений по направлению '+profile.profile.name+' '+profile.profile.edu_prog.qualification.value+' '+profile.eduform+' уже закончился'}
				else:
					result = {'result':0, 'error_msg':'АЛЛО гараж период приема заявлений по направлению '+profile.profile.name+' '+profile.profile.edu_prog.qualification.value+' '+profile.eduform+' еще не начался'}
			#if profileValid >0:

			#FIX DELS	#ApplicationProfiles.objects.filter(application=application).delete()
			"""	
				for i in range(len(forms)):
					appProf = ApplicationProfiles.objects.filter(pk = app_prof_id[i]).first()
					if appProf is None:
						appProf = ApplicationProfiles()
					appProf.application=application		
					appProf.profile=ProfileAttrs.objects.get(pk = forms[i])
					if (application.date >= datetime.datetime.strftime(appProf.profile.startDate,'%Y-%m-%d')):
						if (application.date <= datetime.datetime.strftime(appProf.profile.endDate,'%Y-%m-%d')):
							appProf.save()
							successProfileCount+=1
						else:
							#result = {'result':0, 'error_msg':'АЛЛО гараж дата приема заявлений по направлению '+appProf.profile}
							print("pozdno")
					else:
						#result = {'result':0, 'error_msg':'rano'}	
						print("rano")
			"""

	# if successProfileCount>0:
	# application.save()
	# application.delete()
	return HttpResponse(json.dumps(result), content_type="application/json")


@transaction.atomic
def DeleteApplication(request):
	result = {'result': 0, 'error_msg': ''}
	if request.method == 'GET':
		app = Application.objects.get(pk=request.GET.get('id'))
		app.appState = AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(
			value__icontains=u'Анулированный').first()
		app.track = True
		app.save()
	return HttpResponse(json.dumps(result), content_type="application/json")


@transaction.atomic
def Save_Abiturient(values):
	abit = Abiturient()
	abit.user = User.objects.create_user(username=values.get('username', ''), email=values.get('email', ''),
										 password=values.get('password', ''))
	abit.user.save()
	abit.fname = values.get('fName', '')
	abit.sname = values.get('sName', '')
	abit.mname = values.get('mName', '')
	abit.sex = values.get('sex', '')
	abit.birthdate = datetime.datetime.strptime(values.get('birthday', ''), '%d/%m/%Y').strftime('%Y-%m-%d')
	abit.save()


def rpHash(person):
	hash = 5381
	value = person.upper()
	for caracter in value:
		hash = ((np.left_shift(hash, 5) + hash) + ord(caracter))
	hash = np.int32(hash)
	return hash


def CreatePerson(request):
	result = {'result': 0, 'error_msg': ''}
	if request.method == 'POST':
		if (rpHash(request.POST.get('captcha', '')) == int(request.POST.get('captchaHash', ''))):
			try:
				Save_Abiturient(request.POST)
				username = request.POST.get('username', '')
				password = request.POST.get('password', '')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
			except Exception as e:
				result['result'] = 1
				result['error_msg'] = str(e)  # "Что-то пошло не так."
		else:
			result['result'] = 1
			result['error_msg'] = "Неправильно введена капча!"
	return HttpResponse(json.dumps(result), content_type="application/json")


@transaction.atomic
def AccountInfoChanging(request):
	print(request.POST)
	result = {'result': 0, 'error_msg': ''}
	if request.method == 'POST':
		try:
			# AHAHHAHAHAHAHAHAHAHAH HAHAHAHHAH O BOJE MOI POSCHADITE HAHAHAHAHAHAHAHHAHAHAHAHAHA
			if len(request.POST.get('email', '')) > 0:
				user = request.user
				user.email = request.POST.get('email', '')
				user.save()
			if len(request.POST.get('passwordCurrent', '')) > 0:
				username = request.user.username
				password = request.POST.get('passwordCurrent', '')
				user = authenticate(username=username, password=password)
				if user is None:
					result['result'] = 1
					result['error_msg'] = "Указан неверный пароль."
				else:
					if request.POST.get('passwordNew', '') == request.POST.get('passwordNewVerify', ''):
						user.set_password(request.POST.get('passwordNew', ''))
						user.save()
					else:
						result['result'] = 1
						result['error_msg'] = "Значения нового пароля не совпадают."
		except Exception as e:
			result['result'] = 1
			result['error_msg'] = str(e)  # "Что-то пошло не так."
	return HttpResponse(json.dumps(result), content_type="application/json")


@transaction.atomic
def GetAddressTypeValues(request):
	result = {}
	result['success'] = 0
	if request.method == "POST":
		if request.POST.get('adrstype', '') == "current":
			adrs_type = u'По прописке'
			needed_adrs_type = u'Фактический'
		else:
			adrs_type = u'Фактический'
			needed_adrs_type = u'По прописке'
		abiturient = Abiturient.objects.get(user=request.user)
		adrs = Address.objects.filter(abiturient=abiturient).filter(adrs_type__value__icontains=adrs_type).first()
		if adrs is None:
			adrs = Address()
			adrs.abiturient = abiturient
		adrs.adrs_type = AttrValue.objects.filter(value__icontains=adrs_type).first()
		adrs.zipcode = request.POST.get('adrsindex', '')
		adrs.street = Street.objects.filter(name__icontains=request.POST.get('street', '')).first()
		adrs.house = request.POST.get('adrshouse', '')
		adrs.building = request.POST.get('adrsbuilding', '')
		adrs.flat = request.POST.get('adrsflat', '')
		if ((request.POST.get('adrsisthesame', '')) == "yes"):
			adrs.adrs_type_same = True
			# adrs.adrs_type=AttrValue.objects.filter(value__icontains=u'прописке').first()
			Address.objects.filter(abiturient=abiturient).delete()
		else:
			adrs.adrs_type_same = False
		adrs.save()
		needed_adrs = Address.objects.filter(abiturient=abiturient).filter(
			adrs_type__value__icontains=needed_adrs_type).first()
		if needed_adrs is not None:
			result['success'] = 1
			result['index'] = needed_adrs.zipcode
			result['street'] = needed_adrs.street.name
			result['house'] = needed_adrs.house
			result['building'] = needed_adrs.building
			result['flat'] = needed_adrs.flat
	return HttpResponse(json.dumps(result), content_type="application/json")


def AbiturientList(request):
	Data = {}
	year = datetime.datetime.strftime(datetime.datetime.now(), '%Y')
	abitData = []
	appTypes = AttrValue.objects.filter(attribute__name__icontains=u'Тип договора образования')
	Data['appTypes'] = appTypes

	abitId = [x.application.abiturient.id for x in ApplicationProfiles.objects.filter(profile__year=year)]
	abiturients = Abiturient.objects.filter(id__in=abitId)
	for item in abiturients:
		points = Exams.objects.filter(abiturient=item).aggregate(Sum('points'))
		abitData.append({'abiturient': item, 'points': points.get('points__sum')})
	Data['abitData'] = abitData

	if 'cancel' in request.GET:
		return HttpResponseRedirect(reverse('abiturientList'))

	context = {'data': Data}
	context.update(csrf(request))
	return render(request, 'anketa\\abiturientList.html', context)


################################## AJAX ###################################################

def GetAbiturient(request):
	result = []
	year = datetime.datetime.strftime(datetime.datetime.now(), '%Y')
	abitId = []
	appTypes = AttrValue.objects.filter(attribute__name__icontains=u'Тип договора образования')
	abiturients = Abiturient.objects.all()

	if 'eduprof' in request.GET:
		abitData =[]
		if request.GET['eduprof'] is not None:
			print('eduprof is not None')
			if len(request.GET['eduprof'])>0:
				print('eduprof len > 0')
				abitId = [x.application.abiturient.id for x in ApplicationProfiles.objects.filter(
					profile__year=year).filter(profile__profile__id=int(request.GET['eduprof']))]
				abiturients = abiturients.filter(id__in=abitId)


	if appTypes is not None:
		if len(appTypes) > 0:
			for appT in appTypes:
				appAttrId = [x.app.id for x in Application_attrs.objects.filter(attribute__id=appT.id)]
				print("appAttrId ",appAttrId)
				appProf = ApplicationProfiles.objects.filter(application__id__in=appAttrId).filter(
					profile__profile__id=request.GET['eduprof'])
				print("appProf ",appProf)
				abitId = [x.application.abiturient.id for x in appProf]
				print("abitId ", abitId)
				abiturients = abiturients.filter(id__in=abitId)
				print("abiturients ",abiturients)

				for abitur in abiturients:
					points = Exams.objects.filter(abiturient=abitur).aggregate(Sum('points'))
					print("appT_ID ",appT.id)
					result.append({'abiturient':abitur.fullname,'points':points.get('points__sum'),'appType':appT.id})

	for item in abiturients:
		points = Exams.objects.filter(abiturient=item).aggregate(Sum('points'))
		result.append({'abiturient': item.fullname, 'points': points.get('points__sum')})

	return HttpResponse(json.dumps(result), content_type="application/json")


def Territory(request):
	trry = AttrValue.objects.filter(attribute__id=5)
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")


def District(request):
	dist = AttrValue.objects.filter(attribute__id=7)
	part = request.GET.get('query', '')
	region = request.GET.get('id', '')
	if len(part) > 0:
		dist = dist.filter(value__icontains=part, parent__id=region)
	dist = dist.values('id', 'value')
	result = []
	for item in dist:
		result.append({'id': item['id'], 'value': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def City(request):
	cty = AttrValue.objects.filter(attribute__id=6)
	part = request.GET.get('query', '')
	district = request.GET.get('id', '')
	if len(part) > 0:
		cty = cty.filter(value__icontains=part, parent__id=district)
	cty = cty.values('id', 'value')
	result = []
	for item in cty:
		result.append({'id': item['id'], 'value': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def Streets(request):
	strs = AttrValue.objects.filter(attribute__name__icontains=u'Улица')
	part = request.GET.get('query', '')
	region = request.GET.get('id', '')
	if len(part) > 0:
		strs = strs.filter(value__icontains=part, parent__id=region)
	strs = strs.values('id', 'value')
	result = []
	for item in strs:
		result.append({'id': item['id'], 'value': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def Citizenship(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'гражданство')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id': item['id'], 'text': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def Nation(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'национальность')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id': item['id'], 'text': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def DocType(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'тип документа удостоверяющего личность')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	result = []
	for item in trry:
		result.append({'id': item.id, 'text': item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")


def DocIssuer(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'Выдавший орган')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id': item['id'], 'text': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def EduDocType(request):
	trry = AttrValue.objects.filter(value__icontains=u'диплом') | AttrValue.objects.filter(value__icontains=u'аттестат')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id': item['id'], 'text': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def PrevEduName(request):
	trry = EduOrg.objects.all()
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(name__icontains=part)
	trry = trry.values('id', 'name')
	result = []
	for item in trry:
		result.append({'id': item['id'], 'text': item['name']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def ExamSubject(request):
	subjects = AttrValue.objects.filter(attribute__name__icontains=u'Дисциплина')
	result = []
	for item in subjects:
		result.append({'id': item.id, 'text': item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")


def ExamType(request):
	subjects = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').exclude(value__icontains=u'вступ')
	print(subjects)
	result = []
	for item in subjects:
		result.append({'id': item.id, 'text': item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")


def PrivCat(request):
	privileges = AttrValue.objects.filter(attribute__name__icontains=u'Категория')
	result = []
	for item in privileges:
		result.append({'id': item.id, 'text': item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")


def PrivType(request):
	privileges = AttrValue.objects.filter(attribute__name__icontains=u'Тип привелегии')
	result = []
	for item in privileges:
		result.append({'id': item.id, 'text': item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")


def Achievement(request):
	achievements = AttrValue.objects.filter(attribute__name__icontains=u'Мероприятие')
	result = []
	for item in achievements:
		result.append({'id': item.id, 'text': item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")


def AchievResult(request):
	achievements = AttrValue.objects.filter(attribute__name__icontains=u'Достигнутый результат')
	result = []
	for item in achievements:
		result.append({'id': item.id, 'text': item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")


def Institute(request):
	institute = EduOrg.objects.filter(name__icontains=request.GET.get('query', ''))
	institute = institute.values('id', 'name', 'head')
	result = []
	for item in institute:
		result.append({'id': item['id'], 'text': item['name'], 'head': item['head']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def EduName(request):
	institute = EduOrg.objects.get(pk=request.GET.get('id', ''))
	eduname = institute.education_prog_set.filter(name__icontains=request.GET.get('query', ''))
	eduname = eduname.values('id', 'name', 'qualification__value')
	result = []
	for item in eduname:
		result.append({'id': item['id'], 'text': item['name'] + ' ' + item['qualification__value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def EduProf(request):
	eduname = Education_Prog.objects.get(pk=request.GET.get('id', ''))
	year = datetime.datetime.strftime(datetime.datetime.today(), "%Y")
	# eduprof = eduname.profile_set.filter(name__icontains=request.GET.get('query',''))
	eduprof = eduname.profile_set.filter(name__icontains=request.GET.get('query', ''),
										 profileattrs__year=year).distinct()
	eduprof = eduprof.values('id', 'name')
	result = []
	for item in eduprof:
		result.append({'id': item['id'], 'text': item['name']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def EduName2(request):
	if request.GET['departId'] is not None and len(request.GET['departId']) > 0:
		institute = EduOrg.objects.get(pk=request.GET.get('departId', ''))
	else:
		institute = EduOrg.objects.get(pk=request.GET.get('depHeadId', ''))
	eduname = institute.education_prog_set.filter(name__icontains=request.GET.get('query', ''))
	eduname = eduname.values('id', 'name', 'qualification__value')
	result = []
	for item in eduname:
		result.append({'id': item['id'], 'text': item['name'] + ' ' + item['qualification__value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def EduProfForm(request):
	# eduname = Education_Prog.objects.get(pk = request.GET.get('id',''))
	# добавить фильтр по году
	year = datetime.datetime.strftime(datetime.datetime.today(), "%Y")
	eduprof = Profile.objects.get(pk=request.GET.get('id', ''))
	# eduprof = eduprof.values('id', 'eduform')
	result = []
	for item in eduprof.profileattrs_set.filter(year=year):
		# if item.year == int(year):
		# item['eduform'] = [x[1] for x in EduForm if x[0] == item['eduform']][0]
		result.append({'id': item.id, 'text': item.eduform})
	return HttpResponse(json.dumps(result), content_type="application/json")


def PrivilegiesFunc(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'выдавший')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")


def Rank(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'Воинское')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id': item['id'], 'text': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def Flang(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'Изучаемый')
	part = request.GET.get('query', '')
	if len(part) > 0:
		trry = trry.filter(value__icontains=part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id': item['id'], 'text': item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")


def api_exams(request):
	result = {'result': 0, 'msg': ''}
	if request.method == 'POST':
		if request.POST['action'] == 'delete':
			try:
				Exams.objects.filter(pk=request.POST['id']).delete()
				result['result'] = 1
				result['id'] = request.POST['id']
			except Exception as e:
				result['msg'] = str(e)
	return HttpResponse(json.dumps(result), content_type="application/json")


def api_privileges(request):
	result = {'result': 0, 'msg': ''}
	if request.method == 'POST':
		if request.POST['action'] == 'delete':
			try:
				Privilegies.objects.filter(pk=request.POST['id']).delete()
				result['result'] = 1
				result['id'] = request.POST['id']
			except Exception as e:
				result['msg'] = str(e)
	return HttpResponse(json.dumps(result), content_type="application/json")


def api_achievs(request):
	result = {'result': 0, 'msg': ''}
	if request.method == 'POST':
		if request.POST['action'] == 'delete':
			try:
				Achievements.objects.filter(pk=request.POST['id']).delete()
				result['result'] = 1
				result['id'] = request.POST['id']
			except Exception as e:
				result['msg'] = str(e)
	return HttpResponse(json.dumps(result), content_type="application/json")
