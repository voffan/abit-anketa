
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django import template

import json
from datetime import date
from staff.models import Employee, Position, Contacts as ContactsStaff
from anketa.models import Department, Attribute, AttrType, Application, Abiturient, Docs, AttrValue, Profile, Contacts, Address, Education_Prog, Education_Prog_Form, Privilegies, Exams, DepAchieves, Milit, DocAttr, Achievements
from django.contrib.auth.models import User

# Create your views here.
register = template.Library()

def CheckUserIsStaff:
	return true

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def index(request):
	n = 'Anufriev'
	if request.method == 'POST':
		n = request.POST['input1']
	return render(request,'staff\staff_index.html',{'data':{'username':'nik'}}.update(csrf(request)))

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def login(request):
		args = {}
		args.update(csrf(request))
		if request.POST:
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('/staff/application_list/') # Was '/staff/news'
			else:
					args['login_error'] = "Пользователь не найден"
					return render_to_response('staff\staff_index.html', args)



@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def logout(request):
	if request.POST:
		auth.logout(request)
		return redirect('/staff/')

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Employee_list(request):
	if request.method == 'POST':
		if 'Delete' in request.POST:
			ids = request.POST.getlist('selected')
			return HttpResponseRedirect(reverse('staff:employee_list'))
		elif 'Add' in request.POST:
			return HttpResponseRedirect(reverse('staff:employee_add'))
		elif 'test' in request.POST:
			return HttpResponse('test')
		else:
			return HttpResponse('Employee fired')
	employee_manage = Employee.objects.all()
	data={}
	data['employee'] = employee_manage
	context = {'data':data}
	context.update(csrf(request))
	return render(request,'staff\employee_manage.html',  context)

@transaction.atomic
@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Add_Employee(values):
	empl_id = values.get('user-id','')
	if len(empl_id)>0:
		employee = Employee.objects.get(pk=empl_id)
		user = employee.user
		user.email = values.get('email','')
		user.save()
	else:
		user = User.objects.create_user(values['username'], values['email'],values['password'])
		employee = Employee()
		employee.user = user
	dep = Department.objects.get(pk=values['department'])
	posit = Position.objects.get(pk=values['position'])
	employee.department = dep
	employee.first_name = values.get('fname','')
	employee.last_name = values.get('lname','')
	employee.mid_name = values.get('mname','')
	employee.uniemployee = 0
	employee.position = posit
	employee.save()

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def AddEmployee(request):
	if request.method == 'POST':
		try:
			Add_Employee(request.POST)
		except Exception as e:
			raise e
		return HttpResponseRedirect(reverse('staff:employee_list'))

	positions = Position.objects.all()
	departments = Department.objects.all()
	Data={}
	Data['departments'] = departments
	Data['positions'] = positions
	context = {'data':Data}
	context.update(csrf(request))
	return render(request,'staff\employee_add.html',context)

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def EditEmployee(request, employee_id):
	departments = Department.objects.all()
	employee = Employee.objects.get(pk=employee_id)
	positions = Position.objects.all()
	Data={}
	Data['departments'] = departments
	Data['employee']=employee
	Data['positions']=positions
	context = {'data':Data}
	context.update(csrf(request))
	return render(request,'staff\employee_add.html',context)

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def AddContact(employee, contacts):
	for item in contacts:
		contact = ContactsStaff()
		contact.employee = employee
		contact.contact_type = AttrValue.objects.get(pk=item['id'])
		contact.value = item['value']
		contact.save()

@transaction.atomic
@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def save_user_profile(user, values):
	user.email = values.get('email','')
	password2 = values['confirm']
	password1 = values['password']
	if password1 == password2 and len(password1) > 0:
		user.set_password(values['password'])
	elif len(password1) > 0:
		raise Exception(u'Пароль и подтверждение не совпадают!!')
	user.save()  
	employee = user.employee_set.get() 
	employee.first_name = values.get('fname','')
	employee.last_name = values.get('lname','')
	employee.mid_name = values.get('mname','')
	if len(values['contacts'])>0:	
		AddContact(employee,[{'id':AttrValue.objects.get(attribute__name__icontains=u'контакт', value__icontains=values.get('contacts_type')).id,'value':values.get('contacts','')}])
	employee.save()

@login_required(login_url='/login/')
@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Employee_Useraccount(request):
	user = request.user
	contacts = user.employee_set.get().contacts_set.all()
	error_message = ''
	Data={}	
	if 'save' in request.POST:
		try:
			#сохранить старые значения user и employee
			#sid = transaction.savepoint()
			save_user_profile(request.user, request.POST)
			Data['success_message'] = u'Успешно изменено'
		except Exception as e:
			error_message = str(e)
			transaction.rollback()
			#восстановить старые значения
		
	Data['contacts']=contacts
	Data['contact_type']=AttrValue.objects.filter(attribute__name__icontains=u'контакт')
	Data['employee']=user.employee_set.get() 
	Data['user']=user
	if len(error_message) > 0:
		Data['error_message'] = error_message

	context = {'data':Data}
	context.update(csrf(request))
	return render(request,'staff\employee_acc.html',context)

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Application_list (request):
	applications = Application.objects.all()
	#employee = request.user.employee_set.get()
	#applications = Application.objects.select_related('Abiturient').filter(department__id = employee.department.id)
	#profiles = Profile.objects.all()
	select = '0'
	selectform = '1'
	selectnapr = '0'
	selectdoc = '0'
	selectcopy = '0'
	fname = '0'
	bal1 = '0'
	bal2 = '0'
	dategt = '2016-01-01'
	datelt = '0'     
	filters={'apply':''}

	if 'apply' in request.GET:

		if 'doctype' in request.GET and int(request.GET['doctype'])>0:
				selectdoc = request.GET['doctype']
				docs = Docs.objects.select_related('Abiturient').filter(docType__id=selectdoc)
				abiturients = [item.abiturient.id for item in docs]
				applications = Application.objects.filter(abiturient__id__in=abiturients)
				filters['doctype']=int(selectdoc)

		if 'iscopy' in request.GET:
			if request.GET['iscopy'] =='1':
				selectcopy = '1'
				docs = Docs.objects.select_related('Abiturient').filter(isCopy=0)
				abiturients = [item.abiturient.id for item in docs]
				applications = applications.filter(abiturient__id__in=abiturients) 
				filters['iscopy'] = selectcopy

			elif request.GET['iscopy'] =='2':
				selectcopy = '2'
				docs = Docs.objects.select_related('Abiturient').filter(isCopy=1)
				abiturients = [item.abiturient.id for item in docs]
				applications = applications.filter(abiturient__id__in=abiturients)
				filters['iscopy'] = selectcopy

		if 'status' in request.GET and int(request.GET['status'])>0:
			select = request.GET['status']
			applications = applications.filter(appState__id=select)
			filters['status']= int(select)

		if 'fio' in request.GET and len(request.GET['fio'])>0:
			fname = request.GET['fio']
			applications=applications.filter(abiturient__fullname__icontains=fname)
			filters['fio'] = fname

		if 'forma' in request.GET:
			if request.GET['forma'] =='2':
				applications = applications.filter(edu_prog__eduform__icontains=u'О')
				selectform = '2'
				filters['forma'] = selectform
			if request.GET['forma'] =='3':
				applications = applications.filter(edu_prog__eduform__icontains=u'З')
				selectform = '3'
				filters['forma'] = selectform
			if request.GET['forma'] =='4':
				applications = applications.filter(edu_prog__eduform__icontains=u'ОЗ')
				selectform = '4'
				filters['forma'] = selectform


		if 'balli1' in request.GET and len(request.GET['balli1'])>0:
			bal1 = request.GET['balli1']
			applications = applications.filter(points__gt=bal1)
			filters['balli1'] = bal1

		if 'balli2' in request.GET and len(request.GET['balli2'])>0:
			bal2 = request.GET['balli2']
			applications = applications.filter(points__lt=bal2)
			filters['balli2'] = bal2

		if 'datedoc1' in request.GET and len(request.GET['datedoc1'])>0:
			dategt = request.GET['datedoc1']
			applications = applications.filter(date__gt=dategt)
			filters['datedoc1'] = dategt

		if 'datedoc2' in request.GET and len(request.GET['datedoc2'])>0:
			datelt = request.GET['datedoc2']
			applications = applications.filter(date__lt=datelt)
			filters['datedoc2'] = datelt


		if 'napravlenie' in request.GET and int(request.GET['napravlenie'])>0:
			selectnapr = request.GET['napravlenie']
			applications = applications.filter(edu_prog__edu_prog__id=selectnapr)
			filters['napravlenie'] = int(selectnapr)


	if 'cancel' in request.GET:
		return HttpResponseRedirect(reverse('staff:application_list'))


	
	app_pages = Paginator(applications, 2)

	page = request.GET.get('page')
	try:
		current_page = app_pages.page(page)
	except PageNotAnInteger:
		current_page = app_pages.page(1)
	except EmptyPage:
		current_page = app_pages.page(app_pages.num_pages)

	applications = current_page.object_list
	
	abiturients = [app.abiturient.id for app in applications]


	docs = Docs.objects.select_related('AttrValue').filter(abiturient__id__in = abiturients, docType__value__icontains=u'аттестат')|Docs.objects.select_related('AttrValue').filter(abiturient__id__in = abiturients, docType__value__icontains=u'Диплом')
	

	apps_with_docs=[]
	for app in applications:
		doc = docs.filter(abiturient__id = app.abiturient.id).first()
		apps_with_docs.append({'app':app, 'doc':doc})
	
	doctyps = AttrValue.objects.filter(
		attribute__name__icontains=u'тип док'
	).filter(
		value__icontains=u'Диплом'
	)|AttrValue.objects.filter(
		value__icontains=u'Аттестат'
	)

	data={}
	data['applications'] = apps_with_docs
	data['docType'] = doctyps
	data['Profile'] = Education_Prog.objects.all()
	data['Docs'] = Docs.objects.all()
	data['Application'] = AttrValue.objects.filter(attribute__name__icontains=u'статус за')
	data['pages'] = current_page    
	data['filters'] = filters    
	return render(request,'staff\\application_list.html', data)


@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Application_review (request, application_id):
	if request.method =='POST':
		return HttpResponseRedirect(reverse('staff:application_list'))
	application = Application.objects.select_related('Abiturient').get(pk=application_id)
	#passp = AttrValue.objects.filter(attribute__id = 6)
	
	snils = application.abiturient.docs_set.filter(docType__value__icontains=u'СНИЛС').first()
	passp = application.abiturient.docs_set.filter(docType__value__icontains=u'Паспорт').first()
	if passp is None:
		passp = application.abiturient.docs_set.filter(docType__value__icontains=u'Загран').first()
	if passp is None:
		passp = application.abiturient.docs_set.filter(docType__value__icontains=u'Водит').first()
	if passp is None:
		passp = application.abiturient.docs_set.filter(docType__value__icontains=u'Военн').first()
	
	Data={}
	edu_doc = application.abiturient.docs_set.filter(docType__value__icontains=u'Аттестат').first()
	if edu_doc is not None:
		Data['level'] = 1
	else:
		edu_doc = application.abiturient.docs_set.filter(docType__value__icontains=u'диплом').first()
		level = edu_doc.docattr_set.filter(attr__value__icontains = u'Уровень').first()
		if level is not None and level.value == u'НПО':
			Data['level'] = 2
		if level is not None and level.value == u'СПО':
			Data['level'] = 3
		if level is not None and level.value == u'ВПО':
			Data['level'] = 4

	adrtype = AttrValue.objects.filter(attribute__name__icontains=u'Тип адреса')
	rank = AttrValue.objects.filter(attribute__name__icontains=u'Воинское звание')
	snils = application.abiturient.docs_set.filter(docType__value__icontains=u'СНИЛС').first()
	foreign_lang = AttrValue.objects.filter(attribute__name__icontains=u'иностранный язык')
	docissuer = AttrValue.objects.filter(attribute__name__icontains=u'выдавший ')
	nationality = AttrValue.objects.filter(attribute__name__icontains=u'национальность')
	doctype = AttrValue.objects.exclude(value__icontains=u'диплом').exclude(value__icontains=u'аттест').exclude(value__icontains=u'СНИЛС').filter(attribute__name__icontains=u'тип документа')
	Data['edudoctype'] = AttrValue.objects.filter(value__icontains=u'диплом')|AttrValue.objects.filter(value__icontains=u'аттестат')
	contactyp = AttrValue.objects.filter(attribute__name__icontains=u'Тип контакта')
	#abiturient = application.abiturien_set.filter(attribute__name__icontains=u'Тип контакта')
	Data['nationality'] = nationality
	Data['docType'] = doctype
	Data['docissuer'] = docissuer
	Data['adrtype'] = adrtype
	Data['snils'] = snils
	Data['foreign_lang'] = foreign_lang
	Data['passp'] = passp
	Data['rank'] = rank
	Data['snils'] = snils
	Data['edud'] = edu_doc
	Data['application']=application
	Data['contacts'] = Contacts.objects.filter(person_id=application.abiturient.id)
	Data['address'] = Address.objects.filter(pk=application_id)
	Data['education_prog'] = Education_Prog.objects.filter(pk=application_id)
	Data['exams'] = Exams.objects.filter(pk=application_id)
	Data['privilegies'] = Privilegies.objects.filter(pk=application_id)
	Data['depachieves'] = DepAchieves.objects.filter(pk=application_id)
	if hasattr(application.abiturient, 'milit'):
		Data['milit'] = application.abiturient.milit
	Data['docattr'] = DocAttr.objects.filter(pk=application_id)
	Data['achievements'] = Achievements.objects.filter(pk=application_id)
	
	Data['contactyp'] = contactyp
	print(Data['address'])
	context = {'data':Data}
	context.update(csrf(request))
	return render(request,'staff\\wizardform.html',context)

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def attribute_dels(values):
	dels = values.getlist('selected')
	for item in dels:
		attri_bute = Attribute.objects.filter(id=item)
		attri_bute.delete()

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def attrvalue_dels(values):
	dels = values.getlist('selected')
	for item in dels:
		attr_value = AttrValue.objects.filter(id=item)
		attr_value.delete()

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def attribute_add(values):
	if int(values['attr_id'])<0:
		attri_bute = Attribute(name=values['attr_name'],type_id=values['attrtype'])
	else:
		attri_bute = Attribute.objects.get(pk = values['attr_id'])
		attri_bute.name = values['attr_name']
	attri_bute.save()

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def attrvalue_add(attribute, values):
	if int(values['attr_value_id'])<0:
		attr_value_add = AttrValue(value=values['attr_value'], attribute_id=attribute.id)
	else:
		attr_value_add = AttrValue.objects.get(pk=values['attr_value_id'])
		attr_value_add.value = values['attr_value']
	attr_value_add.save()

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Catalogs(request):
	attribute = Attribute.objects.all()
	Data={}
	if request.method == 'POST':

		if 'filter' in request.POST:
			if len(request.POST.get('attribute1'))>0:
				attribute = attribute.filter(id=request.POST['attribute1'])
		if 'reset' in request.POST:
			return HttpResponseRedirect(reverse('staff:catalogs'))

	if 'delete' in request.POST:		
		attribute_dels(request.POST)

	if 'save' in request.POST and len(request.POST.get('attr_name',''))>0:
		attribute_add(request.POST)
	    
	attribute1 = Attribute.objects.all()    
	attrvalue = AttrValue.objects.all()
	attrtype = AttrType.objects.all()
	Data['attribute1'] = attribute1
	Data['attribute'] = attribute
	Data['attrvalue'] = attrvalue
	Data['attrtype'] = attrtype
	context = {'data':Data}
	context.update(csrf(request))	
	return render(request,'staff\catalogs.html', context)

	
@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Catalogs_attrvalue(request, attribute_id):    
	attribute = Attribute.objects.get(pk=attribute_id)
	attrvalue = AttrValue.objects.filter(attribute__id=attribute_id)
	if 'delete' in request.POST:
		attrvalue_dels(request.POST)
	error_message = ''
	if 'save' in request.POST and len(request.POST['attr_value'])>0:
		try:
			attrvalue_add(attribute, request.POST)
		except Exception as e:
			error_message = str(e)
	
	Data={}
	Data['attrvalue'] = attrvalue
	Data['attribute'] = attribute
	Data['error_message'] = error_message
	context = {'data':Data}
	context.update(csrf(request))
	return render(request, 'staff\catalogs_attrvalue.html', context)

#=================================================ajax functions==========================================================


@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Get_Attrs(request):
	result=[]
	attrs=Attribute.objects.all()
	part = request.GET.get('query','')
	if len(part) > 0:
		attrs = attrs.filter(name__icontains = part)
	for item in attrs:
		result.append({'id':item.id, 'text':item.name})
	return HttpResponse(json.dumps(result), content_type="application/json")

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Get_Attr(request):
	text = request.GET.get('attribute_id','')
	item = Attribute.objects.select_related('AttrType').get(pk= text)
	result = [{ 'name':item.name, 'id':item.id ,'type':{'id':item.type.id,'name':item.type.name}}]
	return HttpResponse(json.dumps(result), content_type="application/json")

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Get_Attr_val(request):
	text = request.GET.get('query','')
	attr = AttrValue.objects.select_related('Attribute').get(pk=text)
	result = [{'name':attr.value, 'id':attr.id, 'attribut':attr.attribute.name}]
	return HttpResponse(json.dumps(result),content_type="application/json")

@login_required(login_url = '/login')
@user_passes_test(CheckUserIsStaff, login_url = '/staff/accessdenied')
def Contact_dels(request):
	args = request.POST.get('query','-1')
	contact = ContactsStaff.objects.get(pk=args)
	result = [{'name':contact.value, 'id':contact.id, 'result':1, 'error_message':''}]
	try:
		contact.delete()
	except Exception as e:
		result['result']=0
		result['error_message']=str(e)
	
	return HttpResponse(json.dumps(result),content_type="application/json")
