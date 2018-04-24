from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from staff import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/','staff.views.login', name = 'login'),
	url(r'^logout/','staff.views.logout',name = 'logout'),
	#url(r'^$',views.index,name='index'),
	url(r'^employee_list/',views.Employee_list, name = 'employee_list'),
	url(r'^employee_add/',views.AddEmployee, name = 'employee_add'),
	url(r'^employee_edit/(?P<employee_id>\d+)',views.EditEmployee, name = 'employee_edit'),
	url(r'^employee_useraccount/',views.Employee_Useraccount, name = 'employee_acc'),
	url(r'^$',views.Application_list, name = 'application_list'),
	url(r'^catalogs/',views.Catalogs, name = 'catalogs'),
	url(r'^catalogs_attrvalue/(?P<attribute_id>\d+)',views.Catalogs_attrvalue, name = 'catalogs_attrvalue'),
	url(r'^application_review/(?P<application_id>\d+)',views.Application_review, name = 'application_review'),
	url(r'get_attrs/',views.Get_Attrs,name='get_attrs'),
	url(r'get_attr/',views.Get_Attr,name='get_attr'),
	url(r'get_attr_val/',views.Get_Attr_val,name='get_attr_val'),
	url(r'contact_dels/',views.Contact_dels,name='contact_dels'),
	url(r'wiz_cont_dels/',views.Wiz_cont_dels, name='wiz_cont_dels'),
	url(r'wiz_cont_apply',views.Wiz_cont_apply, name='wiz_cont_apply'),
	url(r'^add_data_to_person/$',views.AddDataToPerson,name="add_data_to_person"),
	url(r'^edu_orgs/',views.Edu_orgs, name='edu_orgs'),
	url(r'^edu_org_progs/(?P<edu_org_id>\d+)',views.Edu_org_progs, name="edu_org_progs"),	
	url(r'^edu_org_prog_profs/(?P<edu_org_prog_id>\d+)', views.Edu_org_prog_profs, name="edu_org_prog_profs"),
	url(r'^edu_org_prog_prof_attr/(?P<edu_org_prog_prof_id>\d+)', views.Edu_org_prog_prof_attr, name="edu_org_prog_prof_attr"),
	url(r'edu_orgs_value/',views.Edu_orgs_value, name="edu_orgs_value"),
	url(r'edu_org_progs/',views.Edu_org_progs_get, name="edu_org_progs_get"),
	url(r'edu_org_prog_profs/',views.Edu_org_prog_profs_get, name="edu_org_prog_profs_get"),
	url(r'edu_org_prog_prof_attr/',views.Edu_org_prog_prof_attr_get, name="edu_org_prog_prof_attr_get"),
	url(r'add_exam_to_person/',views.Add_exam_to_person, name="add_exam_to_person"),
	url(r'exam_list/',views.Exam_list, name="exam_list"),
	url(r'backgrid_collection.json', views.Backgrid_collection, name="backgrid_collection"),
	url(r'test.json', views.testjson, name="testjson"),
	url(r'print_report', views.Report_print, name="print_report")
	

					)