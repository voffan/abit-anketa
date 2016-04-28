# -*- coding: utf-8 -*-
import json
import numpy as np
import datetime

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.forms.formsets import formset_factory
from django.utils import timezone


from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response, render,get_object_or_404
from django.template import RequestContext

from anketa.models import Person, Address, Attribute, AttrValue, Abiturient, Department, Education_Prog, Profile, Application, Education_Prog_Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required

class StartPage(TemplateView):
	template_name = 'anketa/start.html'

def StartApp(request):
	return render(request, 'anketa/wizardform.html')

@login_required(login_url='authapp:index')
def PersonProfile(request):
	args={'currentpage':1}
	args['fname']=request.user
	args['sname']=request.user
	args['mname']=request.user
	args.update(csrf(request))
	return render(request, 'anketa/profile.html', args)

@login_required(login_url='/login')
def PersonData(request):
	args={'currentpage':2}
	return render(request,'anketa/persondata.html',args)

@login_required(login_url='/login')
def Applications(request):
	args={'currentpage':3}
	applications=Application.objects.filter(abiturient__user=request.user)
	args['applications']=applications
	print(args)
	return render(request,'anketa/applicationList.html',args)

@login_required(login_url='/login')
def Account(request):
	args={'currentpage':4}
	args['email'] = request.user.email
	args.update(csrf(request))
	return render(request,'anketa/account.html',args)

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
	trry = AttrValue.objects.filter(attribute__name__icontains=u'тип докумета')
	part = request.GET.get('query','')
	#testData = {id:"docissuer", text:"docissuer"}

def Citizenship(request):
	trry = AttrValue.objects.filter(attribute__name__icontains = u'гражданство')
	part = request.GET.get('query','')
	#testData = {id:"citizenship", text:"citizenship"}
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
	#testData = {id:"docissuer", text:"docissuer"}
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	result = []
	for item in trry:
		result.append({'id':item.id, 'text':item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")
	
def DocType(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'тип докумета')
	part = request.GET.get('query','')
	#testData = {id:"docissuer", text:"docissuer"}
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	result = []
	for item in trry:
		result.append({'id':item.id, 'text':item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")

def DocIssuer(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'выдавший')
	part = request.GET.get('query','')
	#testData = {id:"docissuer", text:"docissuer"}
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	result = []
	for item in trry:
		result.append({'id':item.id, 'text':item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")

def PrevEduName(request):
	trry = AttrValue.objects.filter(attribute__name__icontains=u'выдавший')
	part = request.GET.get('query','')
	#testData = {id:"docissuer", text:"docissuer"}
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	result = []
	for item in trry:
		result.append({'id':item.id, 'text':item.value})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Institute(request):
	institute = Department.objects.filter(name__icontains = request.GET.get('query',''))
	institute = institute.values('id', 'name')
	result = []
	for item in institute:
		result.append({'id':item['id'], 'text':item['name']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduName(request):
	institute = Department.objects.get(pk = request.GET.get('id',''))
	eduname=institute.education_prog_set.filter(name__icontains=request.GET.get('query',''))
	eduname=eduname.values('id','name', 'qualification__value')
	result = []
	for item in eduname:
		result.append({'id':item['id'], 'text':item['name'] + ' ' + item['qualification__value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduProf(request):
	eduname = Education_Prog.objects.get(pk = request.GET.get('id',''))
	eduprof = eduname.profile_set.filter(name__icontains=request.GET.get('query',''))
	eduprof = eduprof.values('id', 'name')
	result = []
	for item in eduprof:
		result.append({'id':item['id'],'text':item['name']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduProfForm(request):
	eduname = Education_Prog.objects.get(pk = request.GET.get('id',''))
	#eduprof = eduname.education_prog_form_set.filter(edu_prog__name__icontains=request.GET.get('query',''))
	eduprof = eduname.education_prog_form_set.all()
	#print(eduprof)
	eduprof = eduprof.values('id', 'eduform')
	#print(eduprof)
	result = []
	for item in eduprof:
		"""
		if item['eduform']=="О":
			item['eduform']="Очное"
		if item['eduform']=="З":
			item['eduform']="Заочное"
		"""
		result.append({'id':item['id'],'text':item['eduform'][0]})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Privilegies(request):
	trry = AttrValue.objects.filter(attribute__id = 16)
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def Rank(request):
	trry = AttrValue.objects.filter(attribute__id = 17)
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def Flang(request):
	trry = AttrValue.objects.filter(attribute__id = 18)
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def SavePerson(request):
	person = Person()
	person.birthdate = datetime.datetime.strftime(request.POST.get('birthday',''),'%Y-%m-%d')
	person.bithplace = request.POST.get('birthplace','')
	person.nationality = get_object_or_404(AttrValue,pk=10)
	person.citizenship = get_object_or_404(AttrValue,pk=9) #foreign attrval
	person.hostel = request.POST.get('hostel','')
	person.foreign_lang = get_object_or_404(AttrValue,pk=18) #foreign attrval
	#person.father = get_object_or_404(AttrValue,pk=18) #foreign self can be null
	#person.mother = get_object_or_404(AttrValue,pk=18) #foreign self can be null
	person.save()

def SaveApplication(request):
	result = {'result':0, 'error_msg':''}
	#print(request.POST)
	if request.method == 'POST':
		application = Application()
		application.abiturient=Abiturient.objects.get(user=request.user)
		application.department = Department.objects.get(pk = request.POST.get('department',''))
		application.edu_prog=Education_Prog_Form.objects.get(pk=request.POST.get('eduform',''))
		application.date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
		application.eduform = "О"
		application.budget = True
		application.withfee = False
		kaketomenyabesit = AttrValue.objects.filter(attribute__name__icontains=u'Статус заявления').filter(value__icontains=u'Поданный').get(value__icontains=u'Подан')
		#print(kaketomenyabesit.value)
		application.appState = kaketomenyabesit
		application.points =100
		application.save()
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
	abit.birthdate=datetime.datetime.strptime(values.get('birthday',''),'%Y-%m-%d')
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