
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from datetime import date

from staff.models import News, Employee
from anketa.models import Department, Attribute 
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
                   return redirect('/staff/news/')
              else:
                       args['login_error'] = "Пользователь не найден"
                       return render_to_response('staff\staff_index.html', args)
        


def logout(request):
    if request.POST:
        auth.logout(request)
        return redirect('/staff/')

def news_list(request):
    #if request.method == 'POST':
        #if 'accc' in request.POST:
         #   loyee_id = request.POST.get('','')
          #  return HttpResponseRedirect(reverse('staff:employee_acc'))
    #employee = Employee.objects.get(pk=empl_id)      
    news = News.objects.all()    
    data={}
    data['news_list']= news
    context = {'data':data}
    return render(request,'staff\\news.html',context)

def news_content(request, news_id):
    news = News.objects.get(pk=news_id)
    data={}
    data['news']= news
    context = {'data':data}
    return render(request,'staff\\news_content.html',context)

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
    

@login_required(login_url='/login/')
def news_create(request):
    if request.method == 'POST':
        news = News()
        empl = Employee.objects.all().first()
        news.employee= request.user.employee_set.get()
        news.NewsName = request.POST.get('name','')
        news.Description = request.POST.get('Description','')
        news.NewsText = request.POST.get('content','')
        news.NewsDate = date.today()
        news.save()
        return HttpResponseRedirect(reverse('staff:news'))
    data={}
    context = {'data':data}
    context.update(csrf(request))
    return render(request,'staff\\news_create.html',context)

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