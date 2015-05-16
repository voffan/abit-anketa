from django.conf.urls import patterns, include, url

from staff import views

urlpatterns = patterns('',
    url(r'^login/','staff.views.login'),
    url(r'^logout/','staff.views.logout'),
    url(r'^$',views.index,name='index'),
    url(r'^news/',views.news_list, name = 'news'),
    url(r'^news_content/(?P<news_id>\d+)',views.news_content, name = 'news_content'),
    url(r'^employee_list/',views.Employee_list, name = 'employee_list'),
    url(r'^employee_add/',views.AddEmployee, name = 'employee_add'),
    url(r'^news_create/',views.news_create, name = 'create'),                  
                      )
