from django.contrib import admin

import kladr.models

# Register your models here.

admin.site.register(kladr.models.Kladr)
admin.site.register(kladr.models.Street)
admin.site.register(kladr.models.Doma)