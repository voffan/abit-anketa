
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction

from datetime import date
from staff.models import Employee, Position
from anketa.models import Department, Attribute, Application, Abiturient, Docs, AttrValue, Profile, Contacts, Address, Education_Prog , Privilegies, Exams, DepAchieves, Milit, DocAttr, Achievements
from django.contrib.auth.models import User

# Create your views here.

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

def AddEmployee(request):
    if request.method == 'POST':
        empl_id = request.POST.get('user-id','')
        if len(empl_id)>0:
            employee = Employee.objects.get(pk=empl_id)
            user = employee.user
            user.email = request.POST.get('email','')
            user.save()
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['email'],request.POST['password'])
            employee = Employee()
            employee.user = user
        dep = Department.objects.get(pk=request.POST['department'])
        posit = Position.objects.get(pk=request.POST['position'])
        employee.department = dep
        employee.first_name = request.POST.get('fname','')
        employee.last_name = request.POST.get('lname','')
        employee.middle_name = request.POST.get('mname','')
        employee.uniemployee = 0
        employee.position = posit
        employee.save()
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

@login_required(login_url='/login/')
def Employee_Useraccount(request):
    #user = employee.user
    #user.email = request.POST.get('email','')
    user = request.user
    data={}
    data['user']=user
    context = {'data':data}
    context.update(csrf(request))
    return render(request,'staff\employee_acc.html',context)

def Employee_Personals(request):
    user = request.user
    employee = user.employee_set.get()
    data = {'employee':employee}
    #employee.first_name = request.POST.get('fname','')
    #employee.last_name = request.POST.get('lname','')
    #employee.middle_name = request.POST.get('mname','')
    #employee.fullname = request.POST.get('fullname','')
    context = {'data':data}
    context.update(csrf(request))
    return render(request, 'staff\employee_personals.html',context)

def Employee_Changepwd(request):
    if request.method == 'POST':
        #только если подтверждение совпадает с паролем
        user = request.user
        user.change_pwd(request.POST['pwd'])
        user.save()
        return HttpResponseRedirect(reverse('staff:employee_acc'))
    return render(request, 'staff\employee_changepwd.html')

def Employee_Info(request):
    #employee.position = request.POST.get('position','')
    departments = Department.objects.all()
    Data={}
    Data['departments'] = departments
    context = {'data':Data}
    context.update(csrf(request))
    return render(request, 'staff\employee_info.html',context)

#@transaction.atomic
#def jopa(request):


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
    filters={}
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


        if 'balli>' in request.GET and len(request.GET['balli>'])>0:
            bal1 = request.GET['balli>']
            applications = applications.filter(points__gt=bal1)
            filters['bal1'] = bal1

        if 'balli<' in request.GET and len(request.GET['balli<'])>0:
            bal2 = request.GET['balli<']
            applications = applications.filter(points__lt=bal2)
            filters['bal2'] = bal2

        if 'datedoc>' in request.GET and len(request.GET['datedoc>'])>0:
            dategt = request.GET['datedoc>']
            applications = applications.filter(date__gt=dategt)
            filters['date1'] = dategt

        if 'datedoc<' in request.GET and len(request.GET['datedoc<'])>0:
            datelt = request.GET['datedoc<']
            applications = applications.filter(date__lt=datelt)
            filters['date2'] = datelt


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
    filters['pages'] = current_page
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
    data['Application'] = AttrValue.objects.filter(attribute__name__icontains=u'статус за')#Application.objects.all()
    data['filters'] = filters    
    return render(request,'staff\\application_list.html', data)

def Application_review (request, application_id):
    if request.method =='POST':
        #save_application(request)
        return HttpResponseRedirect(reverse('staff:application_list'))
    docs = Docs.objects.all()
    application = Application.objects.select_related('Abiturient').get(pk=application_id)
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
    context = {'data':Data}
    context.update(csrf(request))
    return render(request,'staff\\wizardform.html',context)
