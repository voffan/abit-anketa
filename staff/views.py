
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

from datetime import date
from staff.models import Employee, Position
from anketa.models import Department, Attribute, Application, Abiturient, Docs, AttrValue, Profile, Contacts, Address, Education_Prog , Privilegies, Exams, DepAchieves, Milit, DocAttr, Achievements
from django.contrib.auth.models import User

# Create your views here.
register = template.Library()

def index(request):
    n = 'Anufriev'
    if request.method == 'POST':
        n = request.POST['input1']
    return render(request,'staff\staff_index.html',{'data':{'username':'nik'}}.update(csrf(request)))

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



def logout(request):
    if request.POST:
        auth.logout(request)
        return redirect('/staff/')

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

@transaction.atomic
def save_user_profile(user, values):
    user.email = request.POST.get('email','') 
    password2 = request.POST['confirm']
    password1 = request.POST['password']        
    if password1 == password2 and len(password1) > 0:
        user.set_password(request.POST['password'])
    else:
        raise Exception(u'Пароль и подтверждение не совпадают!!')
    user.save()
    employee.first_name = request.POST.get('fname','')
    employee.last_name = request.POST.get('lname','')
    employee.mid_name = request.POST.get('mname','')
    employee.save()

@login_required(login_url='/login/')
def Employee_Useraccount(request):
    departments = Department.objects.all()   
    user = request.user
    employee = user.employee_set.get()
    positions = Position.objects.all()
    alert = 0
    error_message = ''
    if request.method == 'POST':
        try:
            save_user_profile(request.user, request.POST)
        except Exception as e:
            error_message = str(e)
    Data={}
    Data['alert'] = alert
    Data['departments'] = departments
    Data['employee']=employee
    Data['user']=user
    Data['positions']=positions
    if len(error_message) > 0:
        Data['error_message'] = error_message
    else:
        Data['success_message'] = u'Успешно изменено'

    context = {'data':Data}
    context.update(csrf(request))
    return render(request,'staff\employee_acc.html',context)

def Application_list (request):
    applications = Application.objects.all()
    #employee = request.user.employee_set.get()
    #applications = Application.objects.select_related('Abiturient').filter(department__id = employee.department.id)
    profiles = Profile.objects.all()
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
                applications = applications.filter(eduform__icontains=u'О')
                selectform = '2'
                filters['forma'] = selectform
            if request.GET['forma'] =='3':
                applications = applications.filter(eduform__icontains=u'З')
                selectform = '3'
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
                applications = applications.filter(profile__id=selectnapr)
                filters['naprav'] = int(selectnapr)


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
    
    
    data={}
    data['applications'] = apps_with_docs    
    data['docType'] = AttrValue.objects.filter(attribute__name__icontains=u'тип док')
    data['Profile'] = Profile.objects.all()
    data['Docs'] = Docs.objects.all()
    data['Application'] = AttrValue.objects.filter(attribute__name__icontains=u'статус за')
    data['pages'] = current_page    
    data['filters'] = filters    
    return render(request,'staff\\application_list.html', data)


def Application_review (request, application_id):
    if request.method =='POST':
        return HttpResponseRedirect(reverse('staff:application_list'))
    docs = Docs.objects.all()
    application = Application.objects.select_related('Abiturient').get(pk=application_id)
    applications = Application.objects.filter(abiturient__id__in=abiturients)
    Data={}
    Data['docs'] = docs
    Data['application']=application
    Data['contacts'] = Contacts.objects.filter(pk=application_id)
    Data['address'] = Address.objects.filter(pk=application_id)
    Data['education_prog'] = Education_Prog.objects.filter(pk=application_id)
    Data['exams'] = Exams.objects.filter(pk=application_id)
    Data['privilegies'] = Privilegies.objects.filter(pk=application_id)
    Data['depachieves'] = DepAchieves.objects.filter(pk=application_id)
    Data['milit'] = application.abiturient.milit_set.first()
    Data['docattr'] = DocAttr.objects.filter(pk=application_id)
    Data['achievements'] = Achievements.objects.filter(pk=application_id) 
    Data['nationality'] = AttrValue.objects.filter(attribute__name__icontains = u'национальность')   
    data['doctype'] = AttrValue.objects.filter(attribute__name__icontains=u'тип документа')
    data['docissuer'] = AttrValue.objects.filter(attribute__name__icontains=u'Орган выдавший документ')
    data['foreign_lang'] = AttrValue.objects.filter(attribute__name__icontains=u'Изучаемый иностранный язык')
    data['rank'] = AttrValue.objects.filter(attribute__name__icontains=u'Воинское звание')
    
    
    context = {'data':Data}
    context.update(csrf(request))
    return render(request,'staff\\wizardform.html',context)
