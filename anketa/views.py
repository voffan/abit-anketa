import json

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.forms.formsets import formset_factory
from django.utils import timezone

from django.http import HttpResponse

from django.shortcuts import render_to_response, render
from django.template import RequestContext

from anketa.models import Person, Address, Attribute, AttrValue
#from anketa.forms import Person_form, Address_form, Address_coincides_form, EGE_form, Application_form, Milit_form, Is_mil_service_form, Privilegies_form, Need_exams_form	

class StartPage(TemplateView):
    template_name = 'anketa/start.html'

"""
class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'anketa/feedback.html'
    success_url = '/abit-anketa'

def person_add(request):
    person_form = Person_form(request.POST or None)
    AddressFormSet = formset_factory(Address_form, extra=0)
    address_formset = AddressFormSet(request.POST or None, prefix='address', initial=[{}])
    address_coincides_form = Address_coincides_form(request.POST or None)
    is_mil_service_form = Is_mil_service_form(request.POST or None)
    MilitFormSet = formset_factory(Milit_form, extra=1)
    milit_formset = MilitFormSet(request.POST or None, prefix='milit')
    ApplicationFormSet = formset_factory(Application_form, extra=1, max_num=3)
    application_formset = ApplicationFormSet(request.POST or None, prefix='application')
    EGEFormSet = formset_factory(EGE_form, extra=1)
    ege_formset = EGEFormSet(request.POST or None, prefix='ege')
    NeedExamsFormSet = formset_factory(Need_exams_form, extra=1)
    need_exams_formset = NeedExamsFormSet(request.POST or None, prefix='need_exams')
    PrivilegiesFormSet = formset_factory(Privilegies_form, extra=1)
    privilegies_formset = PrivilegiesFormSet(request.POST or None, prefix='privilegies')
    if person_form.is_valid() and address_formset.is_valid() and milit_formset.is_valid() and application_formset.is_valid() and ege_formset.is_valid() and need_exams_formset.is_valid() and privilegies_formset.is_valid():
        person = person_form.save()
        for (counter, address_form) in enumerate(address_formset):
            if address_form.has_changed():
                address = address_form.save(commit = False)
                address.id_person = person
                if 0 == counter:
                    address.id_addr_type = Universal_directory.objects.get(name=u'по прописке',type=Directory_types.objects.get(name="Адрес"))
                elif 1 == counter:
                    address.id_addr_type = Universal_directory.objects.get(name=u'проживания',type=Directory_types.objects.get(name="Адрес"))
                address.save()
        for milit_form in milit_formset:
            if milit_form.has_changed():
                milit = milit_form.save(commit = False)
                milit.id_person = person
                milit.save()
        for application_form in application_formset:
            application = application_form.save(commit = False)
            application.id_person = person
            application.id_pln = Edu_prog.objects.get(id_study_form=application_form.cleaned_data['id_study_form'], id_institute=application_form.cleaned_data['id_institute'], id_specialn=application_form.cleaned_data['id_specialn'], id_spec=application_form.cleaned_data['id_spec'])
            application.date_in = timezone.now()
            application.save()
        for ege_form in ege_formset:
            if ege_form.has_changed():
                ege = ege_form.save(commit = False)
                ege.id_person = person
                ege.save()
        for need_exams_form in need_exams_formset:
            if need_exams_form.has_changed():
                need_exams = need_exams_form.save(commit = False)
                need_exams.id_person = person
                need_exams.save()
        for privilegies_form in privilegies_formset:
            if privilegies_form.has_changed():
                privilegies = privilegies_form.save(commit = False)
                privilegies.id_person = person
                privilegies.save()
        return render_to_response('anketa/id.html', {'person': person}, context_instance=RequestContext(request))
    return render_to_response('anketa/form.html', {'person_form': person_form, 'address_formset': address_formset, 'address_coincides_form': address_coincides_form, 'is_mil_service_form': is_mil_service_form, 'milit_formset': milit_formset, 'application_formset': application_formset, 'ege_formset': ege_formset, 'need_exams_formset': need_exams_formset, 'privilegies_formset': privilegies_formset}, context_instance=RequestContext(request))

def feeds_subcat(request):
    from django.core import serializers
    if "0" == request.GET['id']:
        if "pid" in request.GET:
            if "0" == request.GET['pid']:
                json_subcat = serializers.serialize("json", Universal_directory.objects.filter(parent=None, type=Directory_types.objects.get(name=request.GET['type'])))
            else:
                json_subcat = serializers.serialize("json", Universal_directory.objects.filter(parent=request.GET['pid'], type=Directory_types.objects.get(name=request.GET['type'])))
        else:
            json_subcat = serializers.serialize("json", Universal_directory.objects.filter(parent=None, type=Directory_types.objects.get(name=request.GET['type'])))
    else:
        json_subcat = serializers.serialize("json", Universal_directory.objects.filter(parent=request.GET['id'], type=Directory_types.objects.get(name=request.GET['type'])))
    return HttpResponse(json_subcat, mimetype="application/javascript")

def autocomplete(request):
    from django.core import serializers
    json_subcat = Universal_directory.objects.filter(name__icontains=request.GET['term'], type=Directory_types.objects.get(name=u'Учебное заведение')).values_list('name', flat=True)
    return HttpResponse(json.dumps([unicode(t) for t in json_subcat]), mimetype="application/javascript")
"""

def StartApp(request):
    return render(request, 'anketa/wizardform.html')

def Streets(request):
    strs = Address.objects.all().distinct()
    part = request.POST.get('strs','')
    if len(part)>0:
        strs = strs.filter(street__icontains == part)
    strs = strs.values('street')
    return json.dumps(strs)

def Zipcode(request):
    zpcd = Address.objects.all().distinct()
    part = request.POST.get('zpcd','')
    if len(part)>0:
        zpcd = zpcd.filter(zipcode__icontains == part)
    zpcd = zpcd.values('zipcode')
    return json.dumps(zpcd)

def Territory(request):
    trry = AttrValue.objects.filter(attribute__id = 2)
    part = request.GET.get('query','')
    if len(part)>0:
        trry = trry.filter(value__icontains = part)
    trry = trry.values('id', 'value')
    result = []
    for item in trry:
        result.append(item)
    return HttpResponse(json.dumps(result), content_type="application/json")

def District(request):
    dist = AttrValue.objects.filter(attribute__id = 3)
    part = request.GET.get('query','')
    region = request.GET.get('id','')
    if len(part)>0:
        dist = dist.filter(value__icontains = part, parent__id = region)
    dist = dist.values('id', 'value')
    result = []
    for item in dist:
        result.append({'id':item['id'],'value':item['value']})
    return HttpResponse(json.dumps(result), content_type="application/json")

def City(request):
    cty = AttrValue.objects.filter(attribute__id = 4)
    part = request.GET.get('query','')
    district = request.GET.get('id', '')
    if len(part)>0:
        cty = cty.filter(value__icontains = part, parent__id = district)
    cty = cty.values('id', 'value')
    result = []
    for item in cty:
        result.append({'id':item['id'],'value':item['value']})
    return HttpResponse(json.dumps(result), content_type="application/json")

def Settlement(request):
    settle = Address.objects.all().distinct()
    part = request.POST['settle']
    if len(part)>0:
        settle = settle.filter(settlement__icontains == part)
    settle = settle.values('id','settlement')
    return json.dumps(settle)

