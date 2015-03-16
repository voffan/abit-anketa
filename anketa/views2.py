from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.forms.formsets import formset_factory
from django.utils import timezone
from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext

from anketa.models import *
from anketa.forms import *

import pdb


    
class Application_Wizard(SessionWizardView):
    TEMPLATES = {'0': 'step_name.html', 
    			'1': 'step_document.html', 
    			'2': 'step_education.html',
    			'3': 'step_address.html'}

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })