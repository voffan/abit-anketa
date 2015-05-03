from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from anketa.views import StartPage, StartApp

from anketa.views2 import *

urlpatterns = patterns('',
    url(r'^$', StartPage.as_view()),
    url(r'^application/$', StartApp),
    #url(r'^feedback/$', FeedbackCreateView.as_view()),
    #url(r'^ajax/categ/$', 'anketa.views.feeds_subcat'),
    #url(r'^ajax/autocomplete/$', 'anketa.views.autocomplete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staff/', include('staff.urls',namespace = 'staff')),
    #url(r'^appwizard/', Application_Wizard.as_view([Step_Name, Step_Document, Step_Education, Step_Address])),
)
