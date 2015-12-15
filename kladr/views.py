#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.files import File
from django.db import transaction

from decimal import *
from datetime import date, datetime
#=========================models import===================================================
from kladr.models import Kladr, Street
#=========================auth imports====================================================
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
import json

# Create your views here.

def get_street(request):
	result=[]
	village = request.GET.get('village','')
	query = request.GET.get('query','')
	if len(village)>0:
		village_code = village[:11]
		streets = Street.objects.filter(code__startswith=village_code)
		if len(query)>0:
			streets = streets.filter(name__icontains=query)
		result=[{'id':item.code, 'text':item.name} for item in streets]
	return HttpResponse(json.dumps(result), content_type='application/json')

def get_region(request):
	regions = Kladr.objects.filter(code__iendswith='00000000000')
	query = request.GET.get('query','')
	if len(query)>0:
		regions = regions.filter(name__icontains=query)
	result=[{'id':item.code, 'text':item.name} for item in regions]
	return HttpResponse(json.dumps(result), content_type='application/json')

def get_district(request):
	result=[]
	region = request.GET.get('region','')
	query = request.GET.get('query','')
	if len(region)>0:
		region_code = region[:2]
		district = Kladr.objects.filter(code__startswith=region_code).filter(code__endswith='00000000').exclude(code__iendswith='00000000000')
		if len(query)>0:
			district = district.filter(name__icontains=query)
		result=[{'id':item.code, 'text':item.name} for item in district]
	return HttpResponse(json.dumps(result), content_type='application/json')

def get_homes(request):
	result=[]
	
	return HttpResponse(json.dumps(result), content_type='application/json')

def get_city(request):
	result=[]
	region = request.GET.get('region','')
	query = request.GET.get('query','')
	if len(region)>0:
		region_code = region[:5]
		cities = Kladr.objects.filter(code__startswith=region_code).exclude(code__endswith='00000000000')
		if len(query)>0:
			cities = cities.filter(name__icontains=query)
		result=[{'id':item.code, 'text':item.name} for item in cities]
	return HttpResponse(json.dumps(result), content_type='application/json')

def get_village(request):
	result=[]
	district = request.GET.get('district','')
	query = request.GET.get('query','')
	if len(district)>0:
		district_code = district[:5]
		villages = Kladr.objects.filter(code__startswith=district_code).exclude(code__endswith='00000000')
		if len(query)>0:
			villages = villages.filter(name__icontains=query)
		result=[{'id':item.code, 'text':item.name} for item in villages]
	return HttpResponse(json.dumps(result), content_type='application/json')

def get_village_by_id(street_id):
	object_id = street_id[:11]
	village = Kladr.objects.filter(code__startswith=object_id).first()
	return village

#На вход дается запрос, в котором передается id объекта параметры которого необходимо определить
#Сперва определяем регион, затем район или город, затем нас. пункт и улицу
def get_objects_by_id(request):
	result = []
	query = request.GET.get('id','')
	success = 1
	if len(query)>0:
		object_id = query[:2]+'00000000000'
		region = Kladr.objects.filter(code=object_id).first()
		if region is not None:
			result.append({'data':{'region':{'id':region.code, 'text':region.name},'district':{'id':'','text':''},'city':{'id':'','text':''},'village':{'id':'','text':''},'street':{'id':'','text':''}}})
			object_id = query[2:5]
			if object_id != '000':
				object_id = query[:5]+'00000000'
				district = Kladr.objects.filter(code=object_id).first()
				if district is not None:
					result[0]['data']['district']['id']=district.code
					result[0]['data']['district']['text']=district.name
					village = get_village_by_id(query)
					if village is not None:
						result[0]['data']['village']['id']=village.code
						result[0]['data']['village']['text']=village.name
						street = Street.objects.filter(code=query).first()
						if street is not None:
							result[0]['data']['street']['id']=street.code
							result[0]['data']['street']['text']=street.name
						else:
							error_message = 'Для данного id не соответствует ни одна улица!'
							success = 0
					else:
						error_message = 'Для данного id не соответствует ни один нас. пункт!'
						success = 0
				else:
					error_message = 'Для данного id не соответствует никакой район!'
					success = 0
			else:
				object_id = query[:8]+'00000'
				city = Kladr.objects.filter(code=object_id).first()
				if city is not None:
					result[0]['data']['city']['id']=city.code
					result[0]['data']['city']['text']=city.name
					village_id = query[8:11]
					if village_id != '000':
						village = get_village_by_id(query)
						if village is not None:
							result[0]['data']['village']['id']=village.code
							result[0]['data']['village']['text']=village.name
					street = Street.objects.filter(code=query).first()
					if street is not None:
						result[0]['data']['street']['id']=street.code
						result[0]['data']['street']['text']=street.name
					else:
						error_message = 'Для данного id не соответствует ни одна улица!'
						success = 0
				else:
					error_message = 'Для данного id не соответствует никакой город!'
					success = 0
		else:
			error_message = 'Данного региона не существует!'
			success = 0
	else:
		error_message = 'Дайте идентификатор объекта КЛАДР!'
		success = 0
	if len(result) < 1:
		result.append({})
	result[0]['success'] = success
	if success == 0:
		result[0]['error'] = error_message
	return HttpResponse(json.dumps(result), content_type='application/json')