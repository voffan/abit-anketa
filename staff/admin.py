from django.contrib import admin

# Register your models here.
import staff.models

admin.site.register(staff.models.Contacts)
