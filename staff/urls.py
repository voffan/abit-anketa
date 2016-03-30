from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from staff import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/','staff.views.login', name = 'login'),
    url(r'^logout/','staff.views.logout'),
    url(r'^$',views.index,name='index'),    
    url(r'^employee_list/',views.Employee_list, name = 'employee_list'),
    url(r'^employee_add/',views.AddEmployee, name = 'employee_add'),
    url(r'^employee_edit/(?P<employee_id>\d+)',views.EditEmployee, name = 'employee_edit'),
    url(r'^employee_useraccount/',views.Employee_Useraccount, name = 'employee_acc'),
    url(r'^employee_personals/',views.Employee_Personals, name = 'employee_acc_1'),
    url(r'^employee_changepwd/',views.Employee_Changepwd, name = 'employee_acc_2'),
    url(r'^employee_info/',views.Employee_Info, name = 'employee_acc_3'),
    url(r'^application_list/',views.Application_list, name = 'application_list'),    
    url(r'^application_review/(?P<application_id>\d+)',views.Application_review, name = 'application_review'),
                      )
