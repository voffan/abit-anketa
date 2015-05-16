from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from anketa.views import StartPage, StartApp, Streets, Territory, District, Zipcode, City, Settlement

from anketa.views2 import *

urlpatterns = patterns('',
    url(r'^$', StartPage.as_view()),
    url(r'^application/$', StartApp),
    url(r'^streets/$', Streets, name='streets'),
    url(r'^territory/$', Territory, name = 'territory'),
    url(r'^district/$', District, name = 'district'),
    url(r'^city/$', City , name = 'city'), 
    url(r'^settlement/$', Settlement, name = 'settlement'),
    url(r'^zipcode/$', Zipcode, name = 'zipcode'),
    #url(r'^streets/$',Streets,name='streets'),
    #url(r'^feedback/$', FeedbackCreateView.as_view()),
    #url(r'^ajax/categ/$', 'anketa.views.feeds_subcat'),
    #url(r'^ajax/autocomplete/$', 'anketa.views.autocomplete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staff/', include('staff.urls',namespace = 'staff')),
    #url(r'^appwizard/', Application_Wizard.as_view([Step_Name, Step_Document, Step_Education, Step_Address])),
    url(r'^auth/', include('staff.urls')),
)
