
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
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
                       return render_to_response('staff\\staff_index.html', args)
        


def logout(request):
    auth.logout(request)
    return redirect("/")

def news_list(request):
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
            return HttpResponse('Delete employee')
        elif 'Add' in request.POST:
         
            return HttpResponseRedirect(reverse('staff:employee_add'))
        else:
            return HttpResponse('Employee fired')
    employee_manage = Employee.objects.all()
    data={}
    data['employee'] = employee_manage
    context = {'data':data}
    context.update(csrf(request))
    return render(request,'staff\employee_manage.html',  context)
    '''return render(request,'staff\employee_add.html',  context)'''

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