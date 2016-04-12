import json
import numpy as np 

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.forms.formsets import formset_factory
from django.utils import timezone
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response, render,get_object_or_404
from django.template import RequestContext

from anketa.models import Person, Address, Attribute, AttrValue, Abiturient
from django.contrib.auth.models import User
from django.db import transaction

class StartPage(TemplateView):
    template_name = 'anketa/start.html'

def StartApp(request):
	return render(request, 'anketa/wizardform.html')

def Profile(request):
    args={'currentpage':1}
    return render(request, 'anketa/profile.html', args)

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
    #testData = {id:"citizenship", text:"citizenship"};
    if len(part)>0:
        trry = trry.filter(value__icontains = part)
    #trry = trry.values('id', 'value')
    result = []
    for item in trry:
        result.append({'id':item.id, 'text':item.value})
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
    #trry = trry.values('id', 'value')
    result = []
    for item in trry:
        result.append({'id':item.id, 'text':item.value})
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
    trry = AttrValue.objects.filter(attribute__id = 13)
    part = request.GET.get('query','')
    if len(part)>0:
        trry = trry.filter(value__icontains = part)
    trry = trry.values('id', 'value')
    result = []
    for item in trry:
        result.append(item)
    return HttpResponse(json.dumps(result), content_type="application/json")

def EduProg(request):
    cty = AttrValue.objects.filter(attribute__id = 14)
    part = request.GET.get('query','')
    depart = request.GET.get('id', '')
    if len(part)>0:
        cty = cty.filter(value__icontains = part, parent__id = depart)
    cty = cty.values('id', 'value')
    result = []
    for item in cty:
        result.append({'id':item['id'],'value':item['value']})
    return HttpResponse(json.dumps(result), content_type="application/json")

def EduProf(request):
    cty = AttrValue.objects.filter(attribute__id = 15)
    part = request.GET.get('query','')
    prog = request.GET.get('id', '')
    if len(part)>0:
        cty = cty.filter(value__icontains = part, parent__id = prog)
    cty = cty.values('id', 'value')
    result = []
    for item in cty:
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
	abit.sex=values.get('sexvalue','')
	abit.birthdate=datetime.strptime(values.get('birthday',''),'%Y-%m-%d')
	abit.save()

def CreatePerson(request):
	if request.method =='POST':
		Save_Abiturient(request.POST)
		return HttpResponseRedirect(reverse('application'))
	data={}
	context = {'data':data}
	context.update(csrf(request))
	return render(request,'/',context)

def rpHash(person):
    hash = 5381 
    value = person.upper() 
    print (value)
    for caracter in value: 
        hash = (( np.left_shift(hash, 5) + hash) + ord(caracter)) 
    hash = np.int32(hash)
	#print (hash)
    return hash

def CreatePerson(request):
	if request.method =='POST':
		if (rpHash(request.POST.get('realPerson','')) == request.POST.get('realPersonHash','')):
			try:
				Save_Abiturient(request.POST)
			except Exception as e:
				return HttpResponseRedirect(reverse('profile'))
			return HttpResponseRedirect(reverse('profile'))
		else:
			args={'captcha':'Неправильная капча'}
			return render(request, 'auth/register.html', args)