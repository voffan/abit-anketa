
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage

from datetime import date
from staff.models import Employee
from anketa.models import Department, Attribute, Application, Abiturient, Docs
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
                   return redirect('/staff/') # Was '/staff/news'
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
        employee.department = dep
        employee.first_name = request.POST.get('fname','')
        employee.last_name = request.POST.get('lname','')
        employee.middle_name = request.POST.get('mname','')
        employee.fullname = request.POST.get('fullname','')
        employee.position = request.POST.get('position','')
        employee.save()
        return HttpResponseRedirect(reverse('staff:employee_list'))

    departments = Department.objects.all()
    Data={}
    Data['departments'] = departments
    context = {'data':Data}
    context.update(csrf(request))
    return render(request,'staff\employee_add.html',context)

def EditEmployee(request, employee_id):
    departments = Department.objects.all()
    employee = Employee.objects.get(pk=employee_id)
    Data={}
    Data['departments'] = departments
    Data['employee']=employee
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
    return render(request,'staff\employee_useraccount.html',context)

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
    
def Application_list (request, appl_id):
    employee = request.user.employee_set.get()
    applications = Application.objects.select_related('Abiturient').filter(department__id = employee.department.id)
    number = request.GET.get('page','1')
    app_pages = Paginator(applications, 25)
    try:
        current_page = app_pages.page(number)
    except Exception, e:
        current_page = app_pages.page(1)
    except EmptyPage:
        current_page = app_pages.page(app_pages.num_pages)
    applications = current_page.object_list
    abuturients = [app.abiturient for app in applications]
    docs = Docs.objects.select_related('AttrValue').filter(abiturient__id__in = abiturients, docType__value__icontains='аттестат')|Docs.objects.select_related('AttrValue').filter(abiturient__id__in = abiturients, docType__value__icontains='Диплом')
    apps_with_docs=[]
    for app in applications:
        doc = docs.get(abiturient__id = app.abiturient.id)
        apps_with_docs.append({'app':app, 'doc':doc})
    data={}
    data['applications'] = apps_with_docs
    data.update(csrf(request))
    return render(request,'staff\\application_list.html', data)
