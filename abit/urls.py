from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from anketa.views import StartPage, StartApp, Streets, Territory, District, City, Citizenship, Nation, DocIssuer, PrevEduName, Institute, EduProf, Privilegies, Rank, Flang, CreatePerson, DocType, PersonProfile, Applications, PersonData, Account,EduName, SaveApplication

urlpatterns = patterns('',
    url(r'^$', StartPage.as_view(),name ='startpage'),
    url(r'^profile/$', PersonProfile, name='profile'),
    url(r'^applicationlist/$', Applications, name='applicationList'),
    url(r'^persondata/$', PersonData, name='persondata'),
    url(r'^account/$', Account, name='account'),
    url(r'^application/$', StartApp, name = 'application'),
    url(r'^territory/$', Territory, name = 'territory'),
    url(r'^district/$', District, name = 'district'),
    url(r'^city/$', City , name = 'city'), 
    url(r'^streets/$', Streets, name='streets'),
    url(r'^citizenship/$', Citizenship, name = 'citizenship'),
    url(r'^nation/$', Nation, name = 'nation'),
    url(r'^doctype/$', DocType, name = 'doctype'),
    url(r'^docissuer/$', DocIssuer, name = 'docissuer'),
    url(r'^preveduname/$', PrevEduName, name = 'preveduname'),
    url(r'^institute/$', Institute, name = 'institute'),
    url(r'^eduname/$',EduName,name='eduname'),
    url(r'^eduprof/$', EduProf, name = 'eduprof'),
    url(r'^privilegies/$', Privilegies, name = 'privilegies'),
    url(r'^create_person/$', CreatePerson, name="create_person"),
    url(r'^save_application/$',SaveApplication,name="save_application"),
    url(r'^rank/$', Rank, name = 'rank'),
    url(r'^flang/$', Flang, name = 'flang'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flang/$', Flang, name = 'flang'),
    url(r'^staff/', include('staff.urls',namespace = 'staff')),
    url(r'^auth/', include('authApp.urls', namespace = 'authapp'))
)
