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
	user = authenticate(username=username, password=password)
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

def checkEmailValid(request):
	result = {'result':0, 'error_msg':''}
	email=request.GET.get('email','')
	check = User.objects.filter(email=email).first()

	if check is not None:
		result['result']=1
		result['error_msg']='e-mail занят! Выберете другой'

	return HttpResponse(json.dumps(result), content_type='application/json')

def checkUserValid(request):
	result = {'result':0, 'error_msg':''}
	name=request.GET.get('username','')
	check = User.objects.filter(username=name).first()

	if check is not  None:
		result['result']=1
		result['error_msg']='имя пользователя занято'

	return HttpResponse(json.dumps(result), content_type='application/json')