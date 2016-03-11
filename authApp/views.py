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
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        abiturient=user.abiturient_set.first()
        if abiturient is None:
            return HttpResponseRedirect('/staff')
        else:
            return HttpResponseRedirect('/application')
    else:
        args={'login_error':'Пользователь не найден'}
        return render(request, 'auth/auth.html', args)