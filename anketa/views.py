# -*- coding: utf-8 -*-
import json
import numpy as np
import datetime

from django.views.generic.edit import CreateView
from django.forms.formsets import formset_factory
from django.utils import timezone


from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response, render,get_object_or_404, redirect
from django.template import RequestContext
from kladr.models import Street
from anketa.models import Person, Address, Attribute, AttrValue, Abiturient, EduOrg, ProfileAttrs, ApplicationProfiles, Education_Prog, Profile, Application, EduForm, ApplicationProfiles, Milit, Docs, Exams, DocAttr,Education, Contacts, Relation,\
	Exams_needed
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required


def StartPage(request):
	return render(request,'anketa/start.html')


def StartApp(request):
	return render(request, 'anketa/wizardform.html')

@login_required(login_url='authapp:index')
def PersonProfile(request):
	person=Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	args={'currentpage':1}
	args1=[]
	applications=Application.objects.filter(abiturient__user=request.user).filter(track=True).filter(date__year=datetime.datetime.strftime(datetime.datetime.today(),"%Y"))
	if applications is not None:
		appProf = ApplicationProfiles.objects.all()
		for app in applications:
			prof = appProf.filter(application__id = app.id).first()
			args1.append({'app':app, 'prof':prof})		
		args['applications']=args1
	args.update(csrf(request))
	return render(request, 'anketa/profile.html', args)

@login_required(login_url='authapp:index')
def PersonData(request):
	args={'currentpage':2}
	person=Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	# 1
	args['fname']=person.fname
	args['sname']=person.sname
	args['mname']=person.mname
	args['birthdate']=person.birthdate
	args['sex']=person.sex
	if person.birthplace is not None:
		args['birthplace']=person.birthplace
	if person.citizenship is not None:
		args['citizenship']=person.citizenship.value
		args['citizenship_id']=person.citizenship.id
	if person.nationality is not None:
		args['nationality']=person.nationality.value
		args['nationality_id']=person.nationality.id
	# 2 
	doctype = person.docs_set.filter(docType__attribute__name__icontains=u'удостоверяющего личность').first()
	if doctype is not None:
		args['doctype']=doctype.docType.value
		args['doctype_id']=doctype.docType.id
		args['doctype_serial']=doctype.serialno
		args['doctype_number']=doctype.number
		args['doctype_date']=doctype.issueDate
		args['doctype_issuer_id']=doctype.docIssuer.id
		args['doctype_issuer']=doctype.docIssuer.value
	if person.education_set.first():
		edudoctype = person.education_set.first()
		args['edudoctype']=edudoctype.doc.docType.value
		args['edudoctype_id']=edudoctype.doc.docType.id
		args['edudoctype_serial']=edudoctype.doc.serialno
		args['edudoctype_number']=edudoctype.doc.number
		args['edudoctype_date']=edudoctype.doc.issueDate
		args['edudoctype_issuer_id']=edudoctype.doc.docIssuer.id
		args['edudoctype_issuer']=edudoctype.doc.docIssuer.value
		args['datejoining'] = edudoctype.enterDate
		args['prevedu'] = edudoctype.level.value
	if person.docs_set.filter(docType__value__icontains=u'СНИЛС').first() is not None:
		args['inila']=person.docs_set.filter(docType__value__icontains=u'СНИЛС').first().serialno
	# 3
	address = person.address_set.filter(adrs_type__value__icontains=u'прописке').first()
	if address is not None:
		args['zipcode']=address.zipcode
		args['street']=address.street
		args['house']=address.house
		args['building']=address.building
		args['flat']=address.flat
	contacts_type = AttrValue.objects.filter(attribute__name__icontains=u'Тип контакта')
	if contacts_type is not None:
		args['contacts_type']=contacts_type
	person_contacts = person.contacts_set.all()
	if person_contacts is not None:
		contacts=[]
		for item in person_contacts:
			cont = {}
			cont['type']=item.contact_type
			cont['value']=item.value
			contacts.append(cont)
		args['contacts']=contacts
	relation_type = AttrValue.objects.filter(attribute__name__icontains=u'Тип связи')
	if relation_type is not None:
		args['relation_type']=relation_type
	if Relation.objects.filter(abiturient=person) is not None:
		person_relations = Relation.objects.filter(abiturient=person)
		relations=[]
		for item in person_relations:
			cont = {}
			cont['type']=item.relType
			cont['fio']=item.person.fullname
			cont['value']=Contacts.objects.filter(person=item.person).first().value
			relations.append(cont)
		args['relation']=relations
	# 4
	exams = person.exams_set.exclude(exam_examType__value__icontains=u'вступит')
	if exams is not None:
		examsList=[]
		for item in exams:
			exam={}
			exam['id']=item.id
			exam['subject']=item.exam_subjects.id
			exam['subject_value']=item.exam_subjects.value
			exam['points']=item.points
			exam['year']=item.year
			exam['examtype']={'id':item.exam_examType.id, 'name':item.exam_examType.value}
			examsList.append(exam)
		args['exams']=examsList
	add_exams = person.exams_set.filter(exam_examType__value=u'Вступительный')
	if add_exams is not None:
		specusl= False
		addExamsList=[]
		for item in add_exams:
			exam={}
			exam['id']=item.id
			exam['subject']=item.exam_subjects.id
			exam['subject_value']=item.exam_subjects.value
			exam['points']=item.points
			exam['year']=item.year
			if item.special and specusl == False:
				args['specusl']=True
			addExamsList.append(exam)
		args['addExams']=addExamsList
	# 7 
	args['hostel']=person.hostel
	milit = Milit.objects.filter(abiturient = person).first()
	if milit is not None:
		args['liableForMilit']=milit.liableForMilit
		if milit.liableForMilit==True:
			args['isServed']=milit.isServed
			if milit.isServed==True:
				if milit.rank is not None:
					args['rank']=milit.rank.value
					args['rank_id']=milit.rank.id
				args['yeararmy']=milit.yearDismissial
	if person.foreign_lang is not None:
		args['flang_id']=person.foreign_lang.id
		args['flang']=person.foreign_lang.value
	#print(args)
	args.update(csrf(request))
	return render(request,'anketa/persondata.html',args)

@login_required(login_url='authapp:index')
def Applications(request):
	args={'currentpage':3}
	args1=[]
	year = datetime.datetime.strftime(datetime.datetime.today(),"%Y")
	person=Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	applications=Application.objects.filter(abiturient__user=request.user).filter(date__year=year).exclude(appState = AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(value__icontains = u'Анулированный').first())
	appProf = ApplicationProfiles.objects.all()
	for app in applications:
		prof = appProf.filter(application__id = app.id)
		args1.append({'app':app, 'prof':prof})
	
	args['applications']=args1
	return render(request,'anketa/applicationList.html',args)

@login_required(login_url='authapp:index')
def Account(request):
	args={'currentpage':4}
	person=Abiturient.objects.filter(user=request.user).first()
	if person is None:
		return redirect('/staff')
	args['email'] = request.user.email
	args.update(csrf(request))
	return render(request,'anketa/account.html',args)

def GetSelectedApplication(request):
	result={}
	application = Application.objects.select_related().get(pk = request.GET.get('id',''))
	result['app_num'] = application.id
	result['eduprior']=application.priority
	app_profiles = ApplicationProfiles.objects.select_related().filter(application = application)
	result['department_id']=application.department.id
	result['department_name']=application.department.name
	result['track']=application.track
	result['budget'] = application.budget
	result['withfee'] = application.withfee
	result['edu_prog_id']=app_profiles.first().profile.profile.edu_prog.id
	result['edu_prog_name']=app_profiles.first().profile.profile.edu_prog.name+' ' + app_profiles.first().profile.profile.edu_prog.qualification.value
	result['edu_prog_eduform_id']=app_profiles.first().profile.id
	#result['edu_prog_eduform_name']=[x[1] for x in EduForm if x[0] == app_profiles.first().profile.eduform][0]
	profiles=[]
	for item in app_profiles:
		profiles.append({'id':item.profile.profile.id,'profile':item.profile.profile.name,'eduform':item.profile.eduform, 'prof_attr_id':item.profile.id,'app_prof_id':item.id})
	result['profiles']=profiles
	result['profiles_len']=len(profiles)
	return HttpResponse(json.dumps(result), content_type="application/json")

@transaction.atomic
def SaveExam(request, abit):
	print('Saving Exam!!')
	#if abit.exams_set.filter(exam_examType__value=u'ЕГЭ') is not None:
	#	Exams.objects.filter(abiturient__id=abit.id).filter(exam_examType__value=u'ЕГЭ').delete()
	# abit.exams_set.all().delete a cho ne rabotaet
	examtypes = request.POST.getlist('examType')
	#examtype = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').filter(value__icontains=u'ЕГЭ').first()
	print(request.POST.getlist('examType'))
	exams = request.POST.getlist('egeDisc')
	points = request.POST.getlist('egePoints')
	years = request.POST.getlist('egeYear')
	for i in range(len(exams)):
		subject = AttrValue.objects.filter(attribute__name__icontains=u'Дисциплина').filter(
			pk=exams[i]).first()
		examtype = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').filter(
			pk=examtypes[i]).first()
		#проверить присутствует ли экзамен по типу, дисциплине и году
		exam = Exams.objects.filter(abiturient__id = abit.id, exam_examType = examtypes[i], exam_subjects = exams[i], year = years[i]).first()
		if exam is None:
			exam = Exams()
			exam.abiturient = abit
			exam.exam_examType = examtype
			exam.exam_subjects = subject
			exam.year = years[i]
		exam.points = points[i]
		exam.save()
	if len(request.POST.get('additionalExams', '')) > 0:
		add_exams = request.POST.get('additionalExams', '').split(',')
		specusl = False
		if request.POST.get('specusl', '') == "yes":
			specusl = True
		if abit.exams_set.filter(exam_examType__value=u'Вступительный') is not None:
			Exams.objects.filter(abiturient=abit).filter(exam_examType__value=u'Вступительный').delete()
		for item in add_exams:
			add_exam = Exams()
			add_exam.abiturient = abit
			add_exam.exam_examType = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').filter(
				value__icontains=u'Вступительный').first()
			add_exam.exam_subjects = AttrValue.objects.filter(attribute__name__icontains=u'Дисциплина').filter(
				pk=item).first()
			add_exam.year = datetime.date.today().year
			add_exam.special = specusl
			add_exam.save()
	print('Added!')

@transaction.atomic
def SaveAddress(request, abit):
	print('Saving Address')
	if request.POST.get('adrsisthesame', '') == "yes":
		adrs_type = u'По прописке'
		adrs_fields = ['indexp', 'streetp', 'housep', 'buildingp', 'flatp']
	else:
		adrs_type = u'Фактический'
		adrs_fields = ['indexf', 'streetf', 'housef', 'buildingf', 'flatf']
	if len(request.POST.get(adrs_fields[1], ''))<1:
		print ('returned')
		return
	adrs = Address.objects.filter(abiturient=abit).filter(adrs_type__value__icontains=adrs_type).first()
	if adrs is None:
		adrs = Address()
		adrs.abiturient = abit
	adrs.adrs_type = AttrValue.objects.filter(value__icontains=adrs_type).first()
	adrs.zipcode = request.POST.get(adrs_fields[0], '')
	adrs.street = Street.objects.filter(code=request.POST.get(adrs_fields[1], '')).first()
	adrs.house = request.POST.get(adrs_fields[2], '')
	adrs.building = request.POST.get(adrs_fields[3], '')
	adrs.flat = request.POST.get(adrs_fields[4], '')
	if ((request.POST.get('adrsisthesame', '')) == "yes"):
		adrs.adrs_type_same = True
		# adrs.adrs_type=AttrValue.objects.filter(value__icontains=u'прописке').first()
		Address.objects.filter(abiturient__id=abit.id).delete()
	else:
		adrs.adrs_type_same = False
	adrs.save()
	print('Address saved')

@transaction.atomic
def SaveContacts(request, abit):
	contacttype = request.POST.getlist('contacttype')
	contactvalue = request.POST.getlist('contactvalue')
	if len(contactvalue) < 1 or len(contacttype) < 1:
		return
	if abit.contacts_set.all() is not None:
		Contacts.objects.filter(person=abit).delete()

	for i in range(len(contacttype)):
		if len(contacttype[i]) > 0 and len(contactvalue[i]) > 0:
			#contact = Contacts.objects.filter(person__id = abit.id, contact_type = contacttype[i], value = contactvalue[i]).first()
			#if contact is None:
			contact = Contacts()
			contact.person = abit
			contact.contact_type = AttrValue.objects.filter(pk=contacttype[i]).first()
			contact.value = contactvalue[i]
			contact.save()

@transaction.atomic
def SaveRelevants(request, abit):
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
	SaveAddress(request, abit)
	print('saving contacts')
	SaveContacts(request, abit)
	print('saving relevants')
	SaveRelevants(request, abit)

def AddDataToPerson(request):
	result={'result':"success"}
	#print(request.POST)
	if request.method == 'POST':
		try:
			page=int(request.POST.get('currentPage',''))
			abit=Abiturient.objects.get(user=request.user)
			if abit.info_progress is None:
				abit.info_progress="000000"
			#progress = abit.info_progress.split()
			if page==1: #Личные данные
				#pageIsComplete=True;
				print('Personal')
				abit.sname=request.POST.get('sname','')
				abit.fname=request.POST.get('name','')
				abit.mname=request.POST.get('mname','')
				abit.birthplace=request.POST.get('birthplace','')
				if(len(request.POST.get('birthday','')))>0:
					abit.birthdate=datetime.datetime.strptime(request.POST.get('birthday',''),'%d/%m/%Y').strftime('%Y-%m-%d')
				if(len(request.POST.get('nation','')))>0:
					abit.nationality=AttrValue.objects.get(pk=request.POST.get('nation',''))
				if(len(request.POST.get('citizenship','')))>0:
					abit.citizenship=AttrValue.objects.get(pk=request.POST.get('citizenship',''))
				if(len(request.POST.get('sex','')))>0:
					abit.sex=request.POST.get('sex','')
			if page==2:
				doctype = abit.docs_set.filter(docType__attribute__name__icontains=u'удостоверяющего личность').first()
				if doctype is None:
					doctype=Docs()
					doctype.abiturient=abit
				else:
					doctype.number=None
					doctype.serialno=None
					doctype.issueDate=None
				if(len(request.POST.get('doctype',''))>0):
					doctype.docType=AttrValue.objects.get(pk=request.POST.get('doctype',''))
				if(len(request.POST.get('serialdoc',''))>0):
					doctype.serialno=int(request.POST.get('serialdoc',''))
				if(len(request.POST.get('numberdoc',''))>0):
					doctype.number=int(request.POST.get('numberdoc',''))
				if(len(request.POST.get('datedoc',''))>0):
					doctype.issueDate=datetime.datetime.strptime(request.POST.get('datedoc',''),'%d/%m/%Y').strftime('%Y-%m-%d')
				if(len(request.POST.get('docissuer',''))>0):
					doctype.docIssuer=AttrValue.objects.get(pk=request.POST.get('docissuer',''))
				doctype.save()
				edudoc = abit.education_set.first()
				if edudoc is None:
					edudoc=Education()
					edudoc.abiturient=abit
					doc = Docs()
					doc.abiturient=abit
				else:
					doc = edudoc.doc
				if(len(request.POST.get('edudoctype','')))>0:
					doc.docType=AttrValue.objects.get(pk=request.POST.get('edudoctype',''))
				if(len(request.POST.get('serialedudoc',''))>0):
					doc.serialno=int(request.POST.get('serialedudoc',''))
				if(len(request.POST.get('numberedudoc',''))>0):
					doc.number=int(request.POST.get('numberedudoc',''))
				if(len(request.POST.get('dateexiting',''))>0):
					doc.issueDate=datetime.datetime.strptime(request.POST.get('dateexiting',''),'%d/%m/%Y').strftime('%Y-%m-%d')
				if(len(request.POST.get('preveduname','')))>0:
					doc.docIssuer=AttrValue.objects.get(pk=request.POST.get('preveduname',''))
				doc.save()
				edudoc.doc = doc
				datejoining = request.POST.get('datejoining','')
				if len(datejoining)>0:
					edudoc.enterDate=datetime.datetime.strptime(datejoining,'%d/%m/%Y').strftime('%Y-%m-%d')
				else:
					pageIsComplete=False;
				if doc.docType.value == "Аттестат":
					edudoc.level = AttrValue.objects.filter(attribute__name__icontains=u'Предыдущее образование').filter(value__icontains=u'СОО').first()
				else:
					prevedu = request.POST.get('prevedu','')
					if len(prevedu)>0:
						if prevedu == "npo":
							edudoc.level = AttrValue.objects.filter(attribute__name__icontains=u'Предыдущее образование').filter(value__icontains=u'НПО').first()
						else:
							if prevedu == "spo":
								edudoc.level = AttrValue.objects.filter(attribute__name__icontains=u'Предыдущее образование').filter(value__icontains=u'СПО').first()
							else:
								edudoc.level = AttrValue.objects.filter(attribute__name__icontains=u'Предыдущее образование').filter(value__icontains=u'ВПО').first()
				edudoc.save()
				
				snils = abit.docs_set.filter(docType__value__icontains=u'CНИЛС').first()
				if snils is None:
					snils = Docs()
					snils.docType=AttrValue.objects.filter(value__icontains=u'СНИЛС').first()
					snils.abiturient=abit
				if (len(request.POST.get('inila',''))>0):
					snils.serialno=int(request.POST.get('inila',''))
				snils.docIssuer=doctype.docIssuer
				snils.save()
			
			if page==3:
				SaveContactDetails(request, abit)
			if page==4:
				print('Exams')
				SaveExam(request, abit)
			"""
			if(page==5):

			if(page==6):
			"""
			if page==7:
				if(len(request.POST.get('hostel','')))>0:
					abit.hostel=False
					if(request.POST.get('hostel','')=="yes"):
						abit.hostel=True
				if(len(request.POST.get('flang','')))>0:
					abit.foreign_lang=AttrValue.objects.get(pk=request.POST.get('flang',''))

				if Milit.objects.filter(abiturient = abit).first() is not None:
					Milit.objects.filter(abiturient = abit).first().delete()
				milit = Milit()
				milit.abiturient=abit
				if (len(request.POST.get('liableForMilit','')))>0:
					if request.POST.get('liableForMilit','')=="yes":
						milit.liableForMilit=True
						if (len(request.POST.get('isServed','')))>0:
							if request.POST.get('isServed','')=="yes":
								milit.isServed=True
								if(len(request.POST.get('rank','')))>0:
									milit.rank=AttrValue.objects.get(pk=request.POST.get('rank'))
								if (len(request.POST.get('yeararmy','')))>0:
									milit.yearDismissial=int(request.POST.get('yeararmy',''))
									# АХАХАХАХАХ ХКАКОЙ ККРАСИВЫЙ КОД АХАХАХАХАХХААХХА
				milit.save()

			abit.save()
		except Exception as e:
					result['result']=str(e)
	print('result!')
	return HttpResponse(json.dumps(result), content_type="application/json")

@transaction.atomic
def SaveApplication(request):
	result = {'result':0, 'error_msg':''}	
	if request.method == 'POST':
		if(int(request.POST.get('facepalm',''))>0):
			application=Application.objects.get(pk=request.POST.get('facepalm'))
			if application.appState == AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(value__icontains=u'Подтвержденный').first():
				result = {'result':0, 'error_msg':'zayavlenie yje podtverjdeno nelzya menyat lul'}
				return HttpResponse(json.dumps(result), content_type="application/json")
		else:
			application = Application()
		application.abiturient=Abiturient.objects.get(user=request.user)
		application.department = EduOrg.objects.get(pk = request.POST.get('department',''))
		dateNow = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
		application.date = dateNow
		#application.budget = True
		#application.withfee = False
		app_status = AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(value__icontains=u'Подан').first()
		application.appState = app_status
		application.points =100
		application.priority = request.POST.get('eduprior')
		if request.POST.get('track','') == "false":
			application.track = False
		else:
			application.track = True
		min1 = 0
		if request.POST.get('budget',''):
			application.budget = True
			min1 += 1
		else:
			application.budget = False
		if request.POST.get('withfee',''):
			application.withfee = True
			min1 += 1
		else:
			application.withfee = False			
		if min1 == 0:
			result = {'result':0, 'error_msg':'minimym 1 chek viberi'}
			return HttpResponse(json.dumps(result), content_type="application/json")
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
				points_summ+=i.points
			forms = list(set(forms))
			for i in range(len(forms)):
				profile = ProfileAttrs.objects.get(pk=forms[i])
				if dateNow >= datetime.datetime.strftime(profile.startDate,'%Y-%m-%d'):
					if dateNow <= datetime.datetime.strftime(profile.endDate,'%Y-%m-%d'):						
						application.save()
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

		
		#if successProfileCount>0:
			#application.save()
			#application.delete()		
	return HttpResponse(json.dumps(result), content_type="application/json")

@transaction.atomic
def DeleteApplication(request):
	result = {'result':0, 'error_msg':''}
	if request.method == 'GET':
		app = Application.objects.get(pk=request.GET.get('id'))
		app.appState = AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(value__icontains = u'Анулированный').first()
		app.track = True
		app.save()
	return HttpResponse(json.dumps(result), content_type="application/json")

@transaction.atomic
def Save_Abiturient(values):
	abit = Abiturient()
	abit.user = User.objects.create_user(username=values.get('username',''), email=values.get('email',''), password=values.get('password',''))
	abit.user.save()
	abit.fname=values.get('fName','')
	abit.sname=values.get('sName','')
	abit.mname=values.get('mName','')
	abit.sex=values.get('sex','')
	abit.birthdate=datetime.datetime.strptime(values.get('birthday',''),'%d/%m/%Y').strftime('%Y-%m-%d')
	abit.save()

def rpHash(person):
	hash = 5381 
	value = person.upper() 
	for caracter in value: 
		hash = (( np.left_shift(hash, 5) + hash) + ord(caracter)) 
	hash = np.int32(hash)
	return hash

def CreatePerson(request):
	result = {'result':0, 'error_msg':''}
	if request.method =='POST':
		if (rpHash(request.POST.get('captcha','')) == int(request.POST.get('captchaHash',''))):
			try:
				Save_Abiturient(request.POST)
				username = request.POST.get('username', '')
				password = request.POST.get('password', '')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
			except Exception as e:
				result['result']=1
				result['error_msg']=str(e)#"Что-то пошло не так."
		else:
			result['result']=1
			result['error_msg']="Неправильно введена капча!"
	return HttpResponse(json.dumps(result), content_type="application/json")

@transaction.atomic
def AccountInfoChanging(request):
	print(request.POST)
	result = {'result':0, 'error_msg':''}
	if request.method =='POST':
		try:
			# AHAHHAHAHAHAHAHAHAHAH HAHAHAHHAH O BOJE MOI POSCHADITE HAHAHAHAHAHAHAHHAHAHAHAHAHA
			if len(request.POST.get('email',''))>0:
				user = request.user
				user.email = request.POST.get('email','')
				user.save()
			if len(request.POST.get('passwordCurrent',''))>0:
				username = request.user.username
				password = request.POST.get('passwordCurrent', '')
				user = authenticate(username=username, password=password)
				if user is None:
					result['result']=1
					result['error_msg']="Указан неверный пароль."
				else:
					if request.POST.get('passwordNew','') == request.POST.get('passwordNewVerify',''):
						user.set_password(request.POST.get('passwordNew',''))
						user.save()
					else:
						result['result']=1
						result['error_msg']="Значения нового пароля не совпадают."
		except Exception as e:
				result['result']=1
				result['error_msg']=str(e)#"Что-то пошло не так."
	return HttpResponse(json.dumps(result), content_type="application/json")

@transaction.atomic
def GetAddressTypeValues(request):
	result={}
	result['success']=0
	if request.method == "POST":
		if request.POST.get('adrstype','')=="current":
			adrs_type=u'По прописке'
			needed_adrs_type=u'Фактический'
		else:
			adrs_type=u'Фактический'
			needed_adrs_type=u'По прописке'
		abiturient=Abiturient.objects.get(user=request.user)
		adrs=Address.objects.filter(abiturient=abiturient).filter(adrs_type__value__icontains=adrs_type).first()
		if adrs is None:
			adrs=Address()
			adrs.abiturient=abiturient
		adrs.adrs_type=AttrValue.objects.filter(value__icontains=adrs_type).first()
		adrs.zipcode=request.POST.get('adrsindex','')
		adrs.street=Street.objects.filter(name__icontains=request.POST.get('street','')).first()
		adrs.house=request.POST.get('adrshouse','')
		adrs.building=request.POST.get('adrsbuilding','')
		adrs.flat=request.POST.get('adrsflat','')
		if ((request.POST.get('adrsisthesame','')) == "yes"):
			adrs.adrs_type_same=True
			#adrs.adrs_type=AttrValue.objects.filter(value__icontains=u'прописке').first()
			Address.objects.filter(abiturient=abiturient).delete()
		else:
			adrs.adrs_type_same=False
		adrs.save()
		needed_adrs=Address.objects.filter(abiturient=abiturient).filter(adrs_type__value__icontains=needed_adrs_type).first()
		if needed_adrs is not None:
			result['success']=1
			result['index']=needed_adrs.zipcode	
			result['street']=needed_adrs.street.name
			result['house']=needed_adrs.house
			result['building']=needed_adrs.building
			result['flat']=needed_adrs.flat
	return HttpResponse(json.dumps(result), content_type="application/json")

################################## AJAX ###################################################

def Territory(request):
	trry = AttrValue.objects.filter(attribute__id = 5)
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def District(request):
	dist = AttrValue.objects.filter(attribute__id = 7)
	part = request.GET.get('query','')
	region = request.GET.get('id','')
	if len(part)>0:
		dist = dist.filter(value__icontains = part, parent__id = region)
	dist = dist.values('id', 'value')
	result = []
	for item in dist:
		result.append({'id':item['id'],'value':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def City(request):
	cty = AttrValue.objects.filter(attribute__id = 6)
	part = request.GET.get('query','')
	district = request.GET.get('id', '')
	if len(part)>0:
		cty = cty.filter(value__icontains = part, parent__id = district)
	cty = cty.values('id', 'value')
	result = []
	for item in cty:
		result.append({'id':item['id'],'value':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Streets(request):
	strs =  AttrValue.objects.filter(attribute__name__icontains=u'Улица')
	part = request.GET.get('query','')
	region = request.GET.get('id','')
	if len(part)>0:
		strs = strs.filter(value__icontains = part, parent__id = region)
	strs = strs.values('id', 'value')
	result = []
	for item in strs:
		result.append({'id':item['id'],'value':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Citizenship(request):
	trry = AttrValue.objects.filter(attribute__name__icontains = u'гражданство')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Nation(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'национальность')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")
	
def DocType(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'тип документа удостоверяющего личность')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	result = []
	for item in trry:
		result.append({'id':item.id, 'text':item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")

def DocIssuer(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'выдавший')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduDocType(request):
	trry = AttrValue.objects.filter(value__icontains=u'диплом')|AttrValue.objects.filter(value__icontains=u'аттестат')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def PrevEduName(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'выдавший')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def ExamSubject(request):
	subjects = AttrValue.objects.filter(attribute__name__icontains=u'Дисциплина')
	result = []
	for item in subjects:
		result.append({'id':item.id, 'text':item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")	

def ExamType(request):
	subjects = AttrValue.objects.filter(attribute__name__icontains=u'Тип экзамена').exclude(name__icontains=u'вступ')
	print(subjects)
	result = []
	for item in subjects:
		result.append({'id':item.id, 'text':item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Institute(request):
	institute = EduOrg.objects.filter(name__icontains = request.GET.get('query',''))
	institute = institute.values('id', 'name')
	result = []
	for item in institute:
		result.append({'id':item['id'], 'text':item['name']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduName(request):
	institute = EduOrg.objects.get(pk = request.GET.get('id',''))
	eduname=institute.education_prog_set.filter(name__icontains=request.GET.get('query',''))
	eduname=eduname.values('id','name', 'qualification__value')
	result = []
	for item in eduname:
		result.append({'id':item['id'], 'text':item['name'] + ' ' + item['qualification__value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduProf(request):
	eduname = Education_Prog.objects.get(pk = request.GET.get('id',''))
	year = datetime.datetime.strftime(datetime.datetime.today(),"%Y")
	#eduprof = eduname.profile_set.filter(name__icontains=request.GET.get('query',''))
	eduprof = eduname.profile_set.filter(name__icontains=request.GET.get('query',''), profileattrs__year = year).distinct()
	eduprof = eduprof.values('id', 'name')
	result = []
	for item in eduprof:
		result.append({'id':item['id'],'text':item['name']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduProfForm(request):
	#eduname = Education_Prog.objects.get(pk = request.GET.get('id',''))
	#добавить фильтр по году
	year = datetime.datetime.strftime(datetime.datetime.today(),"%Y")
	eduprof = Profile.objects.get(pk = request.GET.get('id',''))
	#eduprof = eduprof.values('id', 'eduform')
	result = []
	for item in eduprof.profileattrs_set.filter(year = year):
		#if item.year == int(year):	
		#item['eduform'] = [x[1] for x in EduForm if x[0] == item['eduform']][0]
		result.append({'id':item.id,'text':item.eduform})		
	return HttpResponse(json.dumps(result), content_type="application/json")

def Privilegies(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'выдавший')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def Rank(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'Воинское')
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Flang(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'Изучаемый') 
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")