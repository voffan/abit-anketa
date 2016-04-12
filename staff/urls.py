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
	url(r'^application_list/',views.Application_list, name = 'application_list'),
	url(r'^catalogs/',views.Catalogs, name = 'catalogs'),
	url(r'^catalogs_details/(?P<attribute_id>\d+)',views.Catalogs_details, name = 'catalogs_details'),
	url(r'^catalogs_attrtype_add/',views.Catalogs_attrtype_add, name = 'catalogs_attrtype_add'),
	url(r'^catalogs_attrvalue/(?P<attribute_id>\d+)',views.Catalogs_attrvalue, name = 'catalogs_attrvalue'),
	url(r'^catalogs_attrvalue_add/(?P<attribute_id>\d+)',views.Catalogs_attrvalue_add, name = 'catalogs_attrvalue_add'),
	url(r'^catalogs_attribute_add/',views.Catalogs_attribute_add, name = 'catalogs_attribute_add'),
	url(r'^application_review/(?P<application_id>\d+)',views.Application_review, name = 'application_review'),
	url(r'get_attrs/',views.Get_Attrs,name='get_attrs'),
	url(r'get_attrtype/',views.Get_Attrtype,name='get_attrtype'),

					)