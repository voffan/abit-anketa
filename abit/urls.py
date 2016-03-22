from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from anketa.views import StartPage, StartApp, Streets, Territory, District, City, Citizenship, Nation, DocIssuer, PrevEduName, Institute, EduProg, EduProf, Privilegies, Rank, Flang, CreatePerson

from anketa.views2 import *

urlpatterns = patterns('',
    url(r'^$', StartPage.as_view()),
    url(r'^application/$', StartApp, name = 'application'),
    url(r'^territory/$', Territory, name = 'territory'),
    url(r'^district/$', District, name = 'district'),
    url(r'^city/$', City , name = 'city'), 
    url(r'^streets/$', Streets, name='streets'),
    url(r'^citizenship/$', Citizenship, name = 'citizenship'),
    url(r'^nation/$', Nation, name = 'nation'),
    url(r'^docissuer/$', DocIssuer, name = 'docissuer'),
    url(r'^preveduname/$', PrevEduName, name = 'preveduname'),
    url(r'^institute/$', Institute, name = 'institute'),
    url(r'^eduprog/$', EduProg, name = 'eduprog'),
    url(r'^eduprof/$', EduProf, name = 'eduprof'),
    url(r'^privilegies/$', Privilegies, name = 'privilegies'),
    url(r'^create_person/$', CreatePerson, name="create_person"),
    url(r'^rank/$', Rank, name = 'rank'),
    url(r'^flang/$', Flang, name = 'flang'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staff/', include('staff.urls',namespace = 'staff')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^auth/', include('authApp.urls', namespace = 'authapp'))

)
