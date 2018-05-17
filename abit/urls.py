from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

from anketa.views import StartPage, StartApp, Streets, Territory, District, City, Citizenship, Nation, DocIssuer, Achievement, AchievResult, PrivCat, PrivType, PrevEduName, Institute, EduProf, Privilegies, Rank, Flang, CreatePerson, DocType, PersonProfile, Applications, PersonData, Account,EduName, SaveApplication, EduProfForm, GetSelectedApplication,DeleteApplication,AddDataToPerson, EduDocType,GetAddressTypeValues, ExamSubject, ExamType, AccountInfoChanging, AbiturientList, api_exams, api_privileges, api_achievs


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
    url(r'^city/$', City, name = 'city'),
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
    url(r'^examtype/$', ExamType, name='examtype'),
    url(r'^privcat/$', PrivCat, name='privcat'),
    url(r'^privtype/$', PrivType, name='privtype'),
    url(r'^achievement/$', Achievement, name='achievement'),
    url(r'^achievresult/$', AchievResult, name='achievresult'),
    url(r'^eduform/$', EduProfForm, name='eduform'),
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
    url(r'^kladr/', include('kladr.urls',namespace = 'kladr')),
    url(r'^auth/', include('authApp.urls', namespace = 'authapp')),
    url(r'^abiturientList/',AbiturientList,name="abiturientList"),
    #==============API=================================================
    url(r'apiexams/$',api_exams, name='apiexams'),
    url(r'apiprivileges/$',api_privileges, name='apiprivileges'),
    url(r'apiachievs/$',api_achievs, name='apiachievs')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
