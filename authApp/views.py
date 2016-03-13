from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
#from anketa.models import User
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	return render (request, 'auth/auth.html')

def login_user(username, pwd):
    user = authenticate(username=username, password=pwd)
    if user is not None:
        login(request, user)
    return user

def login_web(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = login_user(username, password)
    if user is not None:
        abiturient=user.abiturient_set.first()
        if abiturient is None:
            return HttpResponseRedirect('/staff')
        else:
            return HttpResponseRedirect('/application')
    else:
        args={'login_error':'Пользователь не найден'}
        return render(request, 'auth/auth.html', args)

def checkuser(request):
    return json.dump()