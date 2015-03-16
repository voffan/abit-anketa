from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from anketa.views import StartPage, FeedbackCreateView, person_add

from anketa.views2 import *

urlpatterns = patterns('',
    url(r'^$', StartPage.as_view()),
    url(r'^application/$', person_add),
    url(r'^feedback/$', FeedbackCreateView.as_view()),
    url(r'^ajax/categ/$', 'anketa.views.feeds_subcat'),
    url(r'^ajax/autocomplete/$', 'anketa.views.autocomplete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^appwizard/', Application_Wizard.as_view([Step_Name, Step_Document, Step_Education, Step_Address])),
)
