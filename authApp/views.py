from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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

def checkUser(request):
	name=request.GET.get('username','')
	check = User.objects.filter(username=name)
	return json.dump()