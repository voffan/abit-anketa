
from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf

from staff.models import News

# Create your views here.

def index(request):
    n = 'Anufriev'
    if request.method == 'POST':
        n = request.POST['input1']
    name = 'Double Hello World!!!'
    return render(request,'staff_index.html',{'data':name, 'name':n}.update(csrf(request)))

def login(request):
         args = {}
         args.update(csrf(request))
         if request.POST:
              username = request.POST.get('username', '')
              password = request.POST.get('password', '')
              user = auth.authenticate(username=username, password=password)
              if user is not None:
                   auth.login(request, user)
                   return redirect('/')
              else:
                       args['login_error'] = "pol'zovatel' ne naiden"
                       return render_to_response('staff_index.html', args)
        


def logout(request):
    auth.logout(request)
    return redirect("/")

def news_list(request):
    news = News.objects.all()
    data={}
    data['news_list']= news
    context = {'data':data}
    render(request,'staff\news.html',conext)