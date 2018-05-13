from django.contrib import admin

# Register your models here.
from staff.models import Employee, Position
import anketa.models# import University, Department, AttrType, Attribute, AttrValue


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'abiturient',
        'adrs_type',
        'street',
        'house',
        'building',
        'flat',
        'adrs_type_same',
    )


class DocsAdmin(admin.ModelAdmin):
    list_display = (
        'abiturient',
        'serialno',
        'number',
        'issueDate',
        'isCopy',
        'docType',
        'docIssuer',
    )


class AttrValueAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'attribute',
    )


class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'abiturient',
        'doc',
        'level',
        'enterDate',
        'graduationDate',
    )


class EduOrgAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'head',
        'orgtype',
    )


#staff
#admin.site.register(News)
admin.site.register(Employee)
admin.site.register(Position)
#admin.site.register(Img)
#anketa
admin.site.register(anketa.models.AttrType)
admin.site.register(anketa.models.Attribute)
admin.site.register(anketa.models.AttrValue, AttrValueAdmin)
admin.site.register(anketa.models.Person)
admin.site.register(anketa.models.Application)
admin.site.register(anketa.models.Education_Prog)
admin.site.register(anketa.models.Education, EducationAdmin)
admin.site.register(anketa.models.Profile)
admin.site.register(anketa.models.Docs, DocsAdmin)
admin.site.register(anketa.models.DocAttr)
admin.site.register(anketa.models.Abiturient)
admin.site.register(anketa.models.ApplicationProfiles)
admin.site.register(anketa.models.Contacts)
admin.site.register(anketa.models.Relation)
admin.site.register(anketa.models.ProfileAttrs)
admin.site.register(anketa.models.Exams)
admin.site.register(anketa.models.EduOrg, EduOrgAdmin)
admin.site.register(anketa.models.Address, AddressAdmin)
