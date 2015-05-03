from django.contrib import admin

# Register your models here.
from staff.models import News, Employee
from anketa.models import University, Department

admin.site.register(News)
admin.site.register(Employee)
admin.site.register(University)
admin.site.register(Department)