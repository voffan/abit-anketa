# -*- coding: utf-8 -*-
import json
import numpy as np 

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.forms.formsets import formset_factory
from django.utils import timezone
from datetime import datetime

from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response, render,get_object_or_404
from django.template import RequestContext

from anketa.models import Person, Address, Attribute, AttrValue, Abiturient, Department
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required

class StartPage(TemplateView):
	template_name = 'anketa/start.html'

def StartApp(request):
	return render(request, 'anketa/wizardform.html')

@login_required(login_url='authapp:index')
def Profile(request):
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
	department=AttrValue.objects.filter(attribute__name__icontains=u'Институт/факультет')
	args['department']=department
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
	strs = AttrValue.objects.filter(attribute__id = 8)
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
	#testData = {id:"citizenship", text:"citizenship"}
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def Nation(request):
	trry = AttrValue.objects.filter(attribute__id = 10)
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")
	
def DocType(request):
	trry = AttrValue.objects.filter(attribute__id = 20)
	part = request.GET.get('query','')
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def DocIssuer(request):
	trry = AttrValue.objects.filter(attribute__id = 11)
	part = request.GET.get('query','')
	testData = {id:"docissuer", text:"docissuer"}
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def PrevEduName(request):
	trry = AttrValue.objects.filter(attribute__id = 12)
	part = request.GET.get('query','')
	testData = {id:"preveduname", text:"preveduname"};
	if len(part)>0:
		trry = trry.filter(value__icontains = part)
	trry = trry.values('id', 'value')
	result = []
	for item in trry:
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

def Institute(request):
	print(request.GET)
	institute = Department.objects.filter(name__icontains = request.GET.get('query',''))
	print (institute)
	institute = institute.values('id', 'name')
	#eduprog=institute.education_prog_set.all()
	result = []
	for item in institute:
		result.append({'id':item['id'], 'text':item['name']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduName(request):
	eduname=AttrValue.objects.filter(attribute__name__icontains=u'Направление/специальность')
	part = request.GET.get('query','')
	institute = request.GET.get('id','')
	if len(part)>0:
		eduname = eduname.filter(value__icontains=part, parent__id = institute)
	eduname = eduname.values('id','value')
	result = []
	for item in eduname:
		result.append({'id':item['id'], 'text':item['value']})
	return HttpResponse(json.dumps(result), content_type="application/json")

def EduProf(request):
	eduprof = AttrValue.objects.filter(attribute__id = 15)
	part = request.GET.get('query','')
	eduname = request.GET.get('id', '')
	if len(part)>0:
		eduprof = eduprof.filter(value__icontains = part, parent__id = eduname)
	eduprof = eduprof.values('id', 'value')
	result = []
	for item in eduprof:
		result.append({'id':item['id'],'value':item['value']})
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
	person.birthdate = datetime.strptime(request.POST.get('birthday',''),'%Y-%m-%d')
	person.bithplace = request.POST.get('birthplace','')
	person.nationality = get_object_or_404(AttrValue,pk=10)
	person.citizenship = get_object_or_404(AttrValue,pk=9) #foreign attrval
	person.hostel = request.POST.get('hostel','')
	person.foreign_lang = get_object_or_404(AttrValue,pk=18) #foreign attrval
	#person.father = get_object_or_404(AttrValue,pk=18) #foreign self can be null
	#person.mother = get_object_or_404(AttrValue,pk=18) #foreign self can be null
	person.save()

@transaction.atomic
def Save_Abiturient(values):
	abit = Abiturient()
	abit.user = User.objects.create_user(username=values.get('username',''), email=values.get('email',''), password=values.get('password',''))
	abit.user.save()
	abit.fname=values.get('fName','')
	abit.sname=values.get('sName','')
	abit.mname=values.get('mName','')
	abit.sex=values.get('sex','')
	abit.birthdate=datetime.strptime(values.get('birthday',''),'%Y-%m-%d')
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