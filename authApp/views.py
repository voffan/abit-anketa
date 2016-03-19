import json
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, render
#from anketa.models import User
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	return render (request, 'auth/auth.html')

def login_user(request):
	username = request.GET.get('username', '')
	password = request.GET.get('password', '')
	user = authenticate(username=username, password=pwd)
	if user is not None:
		login(request, user)
	return user

def login_web(request):
	user = login_user(request)
	if user is not None:
		abiturient=user.abiturient_set.first()
		if abiturient is None:
			return HttpResponseRedirect('/staff')
		else:
			return HttpResponseRedirect('/application')
	else:
		args={'login_error':'Пользователь не найден'}
		return render(request, 'auth/auth.html', args)

def register_index(request):
	return render(request, 'auth/register.html')

def checkPasswordsIdentity(request):
	return json.dump()

def checkEmail(request):
	return json.dump()

def checkUserValid(request):
	result = [{'username':{'result':0, 'error_msg':''},'e-mail':{'result':0, 'error_msg':''}, 'pwd':{'result':0, 'error_msg':''}}]
	name=request.GET.get('username','')
	check = User.objects.filter(username=name).first()

	if check is not  None:
		result[0]['username']['result']=1
		result[0]['username']['error_msg']='имя пользователя занято'

	checkemail = None
	email=request.GET.get('email','')
	checkemail=User.objects.filter(email=email).first()
	if checkemail is not None:
		result[0]['e-mail']['result']=1
		result[0]['e-mail']['error_msg']='e-mail занят! Выберете другой!'

	pwd=request.GET.get('password','')
	pwdv=request.GET.get('passwordverify','')
	if pwd != pwdv:
		result[0]['pwd']['result']=1
		result[0]['pwd']['error_msg']='Пароли не совпадают'

	return HttpResponse(json.dumps(result), content_type='application/json')


def checkPersonValid(request):
	result = [{'username':{'result':1, 'error_msg':''},'e-mail':{'result':1, 'error_msg':''}, 'pwd':{'result':1, 'error_msg':''}}]
	name=request.GET.get('username','')
	check = User.objects.filter(username=name).first()
	print(check)
	if check is not  None:
		result[0]['username']['result']=0
		result[0]['username']['error_msg']='имя пользователя занято'
	checkemail = None
	if checkemail is None:
		result[0]['e-mail']['result']=0
		result[0]['e-mail']['error_msg']='e-mail занят! Выберете другой!'
	return HttpResponse(json.dumps(result), content_type='application/json')