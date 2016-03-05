from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from anketa.models import User
from django.core.context_processors import csrf
#from django.contrib.auth.models import User

# Create your views here.

def index(request):
	return render (request, 'auth/auth.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        args['login_error'] = "Пользователь не найден"
        return render(request, 'auth/auth.html', args)