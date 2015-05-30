from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from staff import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/','staff.views.login'),
    url(r'^logout/','staff.views.logout'),
    url(r'^$',views.index,name='index'),
    url(r'^news/',views.news_list, name = 'news'),
    url(r'^news_content/(?P<news_id>\d+)',views.news_content, name = 'news_content'),
    url(r'^employee_list/',views.Employee_list, name = 'employee_list'),
    url(r'^employee_add/',views.AddEmployee, name = 'employee_add'),
    url(r'^news_create/',views.news_create, name = 'create'),       
    url(r'^news_change/(?P<news_id>\d+)',views.News_Change, name = 'news_change'),
)+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
