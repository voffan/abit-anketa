from django.conf.urls import patterns, include, url

from staff import views

urlpatterns = patterns('',
    url(r'^login/','staff.views.login'),
    url(r'^logout/','staff.views.logout'),
    url(r'^$',views.index,name='index'),
)
