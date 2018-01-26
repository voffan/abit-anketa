from django.contrib import admin
import kladr.models


class KladrAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'socr',
		'code',
	)


class StreetAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'socr',
		'code',
	)


admin.site.register(kladr.models.Kladr, KladrAdmin)
admin.site.register(kladr.models.Street, StreetAdmin)
admin.site.register(kladr.models.Doma)
