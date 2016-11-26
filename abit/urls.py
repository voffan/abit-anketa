from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from anketa.views import StartPage, StartApp, Streets, Territory, District, City, Citizenship, Nation, DocIssuer, PrevEduName, Institute, EduProf, Privilegies, Rank, Flang, CreatePerson, DocType, PersonProfile, Applications, PersonData, Account,EduName, SaveApplication, EduProfForm, GetSelectedApplication,DeleteApplication,AddDataToPerson, EduDocType,GetAddressTypeValues, ExamSubject,AccountInfoChanging


urlpatterns = patterns('',
    url(r'^$', StartPage,name ='startpage'),
    url(r'^profile/$', PersonProfile, name='profile'),
    url(r'^applicationlist/$', Applications, name='applicationList'),
    url(r'^persondata/$', PersonData, name='persondata'),
    url(r'^account/$', Account, name='account'),
    url(r'^accountInfoChanging/$', AccountInfoChanging, name='accountInfoChanging'),
    url(r'^application/$', StartApp, name = 'application'),
    url(r'^territory/$', Territory, name = 'territory'),
    url(r'^district/$', District, name = 'district'),
    url(r'^city/$', City , name = 'city'), 
    url(r'^streets/$', Streets, name='streets'),
    url(r'^citizenship/$', Citizenship, name = 'citizenship'),
    url(r'^nation/$', Nation, name = 'nation'),
    url(r'^doctype/$', DocType, name = 'doctype'),
    url(r'^docissuer/$', DocIssuer, name = 'docissuer'),
    url(r'^edudoctype/$',EduDocType,name='edudoctype'),
    url(r'^preveduname/$', PrevEduName, name = 'preveduname'),
    url(r'^institute/$', Institute, name = 'institute'),
    url(r'^eduname/$',EduName,name='eduname'),
    url(r'^eduprof/$', EduProf, name = 'eduprof'),
    url(r'^examsubject/$', ExamSubject, name = 'examsubject'),
    url(r'^eduform/$', EduProfForm, name='eduform'),
    url(r'^privilegies/$', Privilegies, name = 'privilegies'),
    url(r'^create_person/$', CreatePerson, name="create_person"),
    url(r'^add_data_to_person/$',AddDataToPerson,name="add_data_to_person"),
    url(r'^save_application/$',SaveApplication,name="save_application"),
    url(r'^del_application/$',DeleteApplication,name="del_application"),
    url(r'^getapplication/$', GetSelectedApplication,name="getapplication"),
    url(r'^rank/$', Rank, name = 'rank'),
    url(r'^flang/$', Flang, name = 'flang'),
    url(r'^getaddress/$',GetAddressTypeValues,name='getaddress'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flang/$', Flang, name = 'flang'),
    url(r'^staff/', include('staff.urls',namespace = 'staff')),
    url(r'^auth/', include('authApp.urls', namespace = 'authapp'))
)
